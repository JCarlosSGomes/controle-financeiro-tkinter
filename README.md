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

### 📸 Prints

![image](https://github.com/user-attachments/assets/5a3a658d-9e25-42d6-97e0-9ede8629fedf)
![image](https://github.com/user-attachments/assets/99662788-4fd1-4cc9-a802-ce141949a9b0)
![image](https://github.com/user-attachments/assets/4b85cf5e-be7a-4c47-be85-0a7396f1723f)

### 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/JCarlosSGomes/controle-financeiro-tkinter/blob/main/LICENSE) para mais detalhes.

### 🙋 Sobre o autor

Feito com dedicação por [João Carlos](https://github.com/JCarlosSGomes).  
Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-carlos-b70169125/) para trocar ideias, oportunidades ou colaborações!
