from database.conexao import inserir_transacao, buscar_transacoes
from database.conexao import remover_transacao as db_remover_transacao
from database.conexao import calcular_resumo, exportar_transacoes_csv
from rich.console import Console
from rich.table import Table

console = Console()

# Adiciona transação com input do usuário
def adicionar_transacao():
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")
    data = input("Data (AAAA-MM-DD): ")

    inserir_transacao(descricao, valor, categoria, data)
    console.print("[green]Transação adicionada com sucesso![/green]")

# Lista as transações formatadas com Rich
def listar_transacoes():
    transacoes = buscar_transacoes()
    table = Table(title="Transações")

    table.add_column("ID", justify="right")
    table.add_column("Descrição")
    table.add_column("Valor")
    table.add_column("Categoria")
    table.add_column("Data")

    for t in transacoes:
        table.add_row(str(t[0]), t[1], f"R$ {t[2]:.2f}", t[3], t[4])

    console.print(table)

# Remove uma transação pelo ID com confirmação visual
def remover_transacao():
    try:
        id = int(input("Digite o ID da transação que deseja remover: "))
        db_remover_transacao(id)
        console.print(f"[red]Transação ID {id} removida com sucesso![/red]")
    except ValueError:
        console.print("[bold red]ID inválido. Digite um número inteiro.[/bold red]")

# Mostra um resumo financeiro
def mostrar_resumo():
    receitas, despesas, saldo = calcular_resumo()

    console.print("[bold underline cyan]Resumo Financeiro:[/bold underline cyan]\n")
    console.print(f"[green]Total de Receitas: R$ {receitas:.2f}[/green]\n")
    console.print(f"[red]Total de Despesas: R$ {despesas:.2f}[/red]\n")
    cor_saldo = "green" if saldo >= 0 else "red"
    console.print(f"[bold {cor_saldo}]Saldo Atual: R$ {saldo:.2f}[/bold {cor_saldo}]\n")

# Exporta transações para CSV
def exportar_csv():
    nome_arquivo = input("Digite o nome do arquivo CSV (ou pressione Enter para usar o padrão):")
    if not nome_arquivo:
        nome_arquivo = "transacoes_exportadas.csv"
    exportar_transacoes_csv(nome_arquivo)
    console.print(f"[blue]Transações exportadas para '{nome_arquivo}' com sucesso![/blue]")