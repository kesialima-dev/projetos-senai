def calcular_total(itens):
    return sum(preco for _, preco in itens)
def aplicar_desconto(total, desconto = 0):
    return total * (1 - desconto / 100)
def resumo_pedido(itens, desconto = 0):
    total = calcular_total(itens)
    final = aplicar_desconto(total, desconto)
    print(f'Subtotal: R$ {total:.2f}')
    if desconto:
        print(f'Desconto: {desconto}')
    print(f'Total:  R$ {final:.2f}')

carrinho = [
    ("Camiseta", 49.90),
    ("Tênis", 199.90),
    ("Meia", 15.00),
]

resumo_pedido(carrinho, desconto = 10)
# Subtotal: R$264.80
# Desconto: 10%
# Total:    R$

