procurar = input("Pesquisar peça:")
estoque = ["Prego", "Porca", "Arroela", "Parafuso", "Mola"]

for item in estoque:
    if item == procurar: 
        print("Item encontrado no estoque")
        break
else: 
        print("Item não encontrado")
        
        



