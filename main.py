import typer
from services import transacoes_service
from database.conexao import criar_tabela
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

# Garante que a tabela existe antes de começar
criar_tabela()

# Comando para adicionar transação
@app.command()
def adicionar():
    """Adicionar uma nova transação"""
    console.print("Função [bold green]adicionar()[/bold green] executada com sucesso!")
    transacoes_service.adicionar_transacao()

# Comando para listar transações
@app.command()
def listar():
    """Lista todas as transações"""
    transacoes_service.listar_transacoes()

# Comando para remover transações
@app.command()
def remover():
    """Remove uma transação pelo ID"""
    transacoes_service.remover_transacao()

# Comando para mostrar resumo financeiro
@app.command()
def resumo():
    """Exibe um resumo financeiro (receitas, despesas, saldo)"""
    transacoes_service.mostrar_resumo()

# Comando para exportar transações para CSV
@app.command()
def exportar():
    """Exportar todas as transações para um arquivo CSV"""
    transacoes_service.exportar_csv()

# Início da aplicação
if __name__ == "__main__":
    app()