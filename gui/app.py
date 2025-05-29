import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from database import conexao
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

categoria_listada = ["Renda", "Despesa", "Investimento", "Lazer", "Outro"]

class App:
    def __init__(self, master):
        self.master = master
        master.title("Controle Financeiro Pessoal")
        master.geometry("700x400")

        # Botôes
        frame_botoes = tk.Frame(master)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Adicionar", width=15, command=self.adicionar_transacao).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Listar", width=15, command=self.listar_transacoes).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Remover", width=15, command=self.remover_transacao).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Resumo", width=15, command=self.mostrar_resumo).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Gráficos", width=15, command=self.mostrar_grafico).pack(side=tk.LEFT, padx=5)

        #Tabela
        self.tree = ttk.Treeview(master, columns=("ID", "Descrição", "Valor", "Categoria", "Data"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both", pady=10)

    def listar_transacoes(self):
        self.tree.delete(*self.tree.get_children())
        transacoes = conexao.buscar_transacoes()
        for t in transacoes:
            self.tree.insert("", tk.END, values=t)

    def adicionar_transacao(self):
        def salvar():
            descricao = entry_descricao.get()
            valor = float(entry_valor.get())
            categoria = combo_categoria.get()
            data = entry_data.get()

            if categoria not in categoria_listada:
                messagebox.showwarning("Aviso", "Selecione uma categoria válida.")
                return
            if categoria in ["Despesa", "Lazer", "Outro"]:
                valor = -abs(valor) #força negativo
            else:
                valor = abs(valor) #força positivo

            conexao.inserir_transacao(descricao, valor, categoria, data)
            messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")
            top.destroy()
            self.listar_transacoes()

        top = tk.Toplevel(self.master)
        top.title("Adicionar Transação")

        tk.Label(top, text="Descrição").pack()
        entry_descricao = tk.Entry(top)
        entry_descricao.pack()

        tk.Label(top, text="Valor").pack()
        entry_valor = tk.Entry(top)
        entry_valor.pack()

        tk.Label(top, text="Categoria").pack()
        combo_categoria = ttk.Combobox(top, values=categoria_listada, state="readonly")
        combo_categoria.pack()

        tk.Label(top, text="Data (AAAA-MM-DD)").pack()
        entry_data = tk.Entry(top)
        entry_data.pack()

        tk.Button(top, text="Salvar", command=salvar).pack(pady=10)

    def remover_transacao(self):
        item = self.tree.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma transação para remover.")
            return
        
        id_transacao = self.tree.item(item)["values"][0]
        conexao.remover_transacao(id_transacao)
        messagebox.showinfo("Removido", f"Transação ID {id_transacao} removida.")
        self.listar_transacoes()

    def mostrar_resumo(self):
        receitas, despesas, saldo = conexao.calcular_resumo()
        msg = f"Receitas: R$ {receitas:.2f}\nDespesas: R$ {despesas:.2f}\nSaldo: R$ {saldo:.2f}"
        messagebox.showinfo("Resumo Financeiro", msg)

    def listar_transacoes(self):
        self.tree.delete(*self.tree.get_children())

        # Pergunta se deseja filtrar
        resposta = tk.messagebox.askyesno("Filtro", "Deseja filtrar por categoria?")
        if resposta:
            categoria = self.popup_escolher_categoria()
            if not categoria:
                messagebox.showwarning("Aviso", "Nenhuma categoria selecionada.")
                return
            transacoes = conexao.buscar_transacoes_por_categoria(categoria)
        else:
            transacoes = conexao.buscar_transacoes()

        for t in transacoes:
            self.tree.insert("", tk.END, values=t)

    def popup_escolher_categoria(self):
        popup = tk.Toplevel(self.master)
        popup.title("Escolher Categoria")
        popup.geometry("300x150")

        tk.Label(popup, text="Selecione uma categoria:").pack(pady=10)
        combo = ttk.Combobox(popup, values=categoria_listada, state="readonly")
        combo.pack(pady=5)

        resultado = {"categoria": None}

        def confirmar():
            resultado["categoria"] = combo.get()
            popup.destroy()

        tk.Button(popup,text="Confirmar", command=confirmar).pack(pady=10)
        popup.grab_set()
        popup.wait_window()

        return resultado["categoria"]
    
    def mostrar_grafico(self):
        transacoes = conexao.buscar_transacoes()

        categorias = {}
        receitas = 0
        despesas = 0

        for t in transacoes:
            valor = t[2]
            cat = t[3]
            categorias[cat] = categorias.get(cat, 0) + abs(valor)
            if valor > 0:
                receitas += valor
            else:
                despesas += abs(valor)

        if not categorias:
            messagebox.showinfo("Aviso", "Nenhuma transação para exibir no gráfico.")
            return
        
        # Cria janela
        grafico_win = tk.Toplevel(self.master)
        grafico_win.title("Gráfico Financeiro")
        grafico_win.geometry("600x500")

        # Decide quantos gráficos gerar
        if len(categorias) > 0:
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))
            # Gráfico de pizza
            axs[0].pie(categorias.values(), labels=categorias.keys(), autopct='%1.1f%%')
            axs[0].set_title("Distibuição por Categoria")
        else:
            fig, axs = plt.subplots(1, 1, figsize=(5, 4))
            axs = [axs] # transforma em lista para manter índice

        # Gráfico de barras
        axs[1].bar(["Receitas", "Despesas"], [receitas, despesas], color=["green", "red"])
        axs[1].set_title("Receitas vs Despesas")

        # Embutir no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=grafico_win)
        canvas.draw()
        canvas.get_tk_widget().pack() 

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()