#Etapa 1: Recepção do cliente
nome_cliente = input("Por favor, digite o seu nome:""\n")

print(f"OLÁ {nome_cliente}, BEM VINDO À LANCHONETE DEV! É UM PRAZER ATENDER VOCÊ HOJE.\n")   
print("----------------------------\n")  

#Etapa 2: Exibindo o cardápio
print("\n===NOSSO CARDÁPIO===\n")
print("1. Hambúrguer Clássico - R$25.00\n")
print("2. Refrigerante Lata - R$8.00\n")
print("3. Batata Frita - R$12.00\n")
print("==============================\n")

#Etapa 3: Anotando o pedido
qtd_hamburguer = int(input("Quantos hamburgueres você deseja?"))
qtd_refri = int(input("Quantos refrigerantes você deseja?"))
qtd_batata = int(input("Quantas batatas fritas você deseja?"))

#Etapa 4: Cálculos
total_hamburguer = qtd_hamburguer * 25.00
total_refri = qtd_refri * 8.00
total_batata = qtd_batata * 12.00
valor_total = total_hamburguer + total_refri + total_batata

#Etapa 5: Cupom Fiscal
print("\n=========================================\n")
print(" CUPOM FISCAL \n")
print("==========================================")
print(f"Cliente: {nome_cliente} \n")
print(f"Total Hambúrgueres: R$ {total_hamburguer} \n")
print(f"Total Refrigerantes: R$ {total_refri} \n")
print(f"Total Batata Frita: R$ {total_batata} \n")
print("-----------------------------------------\n")
print(f"VALOR TOTAL À PAGAR: R$ {valor_total} \n")
print("===============================\n")

print("Obrigado pela preferência e volte sempre!\n")

      

      
      


      



   

                    