from utilitarios import (
cadastrar_categoria,
cadastrar_transacao,
saldo_total
)

# Categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_viagens = cadastrar_categoria("Viagens")

# Transações
cadastrar_transacao(
    descricao="Salário Jan/2025",
    valor=2000.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Mesada",
    valor=200.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Conta de luz",
    valor=-180.00,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Chapada dos veadeiros",
    valor=-650.00,
    categoria=categoria_viagens
)

total = saldo_total()
print("saldo total:", total)
