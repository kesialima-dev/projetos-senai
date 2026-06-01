n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
soma = n1 + n2 + n3 + n4 
media = soma / 4.0

if media >= 7.0:
    print("Resultado: Aprovado")
elif media >= 5.0:
    print("Resultado: Recuperação")
else:
    print("Reprovado")

print("n\=== RELATÓRIO FINAL ===")
print(f"Nota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Nota 3: {n3}")
print(f"Nota 4: {n4}")
print(f"Média final: {media:.2f}")









      



