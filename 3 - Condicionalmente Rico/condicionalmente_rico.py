# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
novo_saldo = saldo_total - valor_saque

if novo_saldo >= 0:
    print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
else:
    print("Saldo insuficiente. Saque nao realizado!")