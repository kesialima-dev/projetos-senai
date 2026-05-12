# CALCULADORA BÁSICA
print("=== Calculadora ===\n") 

num1 =float(input("Digite o primeiro número:"))
operador = input("Digite o operador: (+, -, /, *)")
num2 =float(input("Digite o segundo número: "))

if operador == "+" :
    print (num1+num2) 
elif operador == "-" :
    print (num1-num2)
elif operador == "/":
    print (num1/num2) 
if (num1 or num2) == "0":
    print ("Não é possível dividir")
elif operador == "*": 
    print (num1*num2)
if (num1 or num2) == "0":
    print ("0")
else:
    print ("Operador inexistente")
    














