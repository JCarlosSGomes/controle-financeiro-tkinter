# 💰 Controle Financeiro Pessoal com Tkinter

![GitHub repo size](https://img.shields.io/github/repo-size/JCarlosSGomes/controle-financeiro-tkinter)
![GitHub last commit](https://img.shields.io/github/last-commit/JCarlosSGomes/controle-financeiro-tkinter)
![GitHub license](https://img.shields.io/github/license/JCarlosSGomes/controle-financeiro-tkinter)

Este é um projeto completo de controle financeiro pessoal desenvolvido em **Python**, com interface gráfica usando **Tkinter** e banco de dados **SQLite**.  
Ele permite adicionar, listar, remover transações, gerar gráficos de análise financeira e exportar relatórios.

---

## 🚀 Funcionalidades

✅ Adicionar transações (receitas, despesas, investimentos, lazer, outros)  
✅ Listar todas as transações  
✅ Filtrar por categoria (com seleção em combobox)  
✅ Resumo financeiro (total de receitas, despesas, saldo)  
✅ Remover transações por ID diretamente na interface  
✅ Gráficos:
- Pizza: distribuição por categoria
- Barras: comparação receitas vs despesas  
✅ Exportação para CSV  
✅ Versão em terminal (Typer + Rich) e versão gráfica (Tkinter)

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.13
- Tkinter
- SQLite
- Matplotlib
- Typer (para comandos no terminal)
- Rich (saída formatada no terminal)

---

## 💻 Como rodar o projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/JCarlosSGomes/controle-financeiro-tkinter.git
cd controle-financeiro-tkinter
```

### 2️⃣ Crie e ative o ambiente virtual

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Instale as dependências

pip install -r requirements.txt

### 4️⃣ Rode a versão gráfica (Tkinter)

python -m gui.app

### 5️⃣ Rode a versão terminal (Typer)

python main.py --help

📸 Prints

