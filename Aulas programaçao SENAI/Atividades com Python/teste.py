valor_compra = 200

if valor_compra < 100:
    desconto = 0 
elif 100 <= valor_compra <= 200:
    desconto = valor_compra * 0.10 # 10% de desconto
else:
    desconto = valor_compra * 0.20 # 20%
    
valor_final = valor_compra - desconto

print (f"valor original: R$ {valor_compra:.2f}")
print (f"desconto aplicado: R$ {desconto:.2f}")
print (f"valor final a pagar: R$ {valor_final:.2f}")



