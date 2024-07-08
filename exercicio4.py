print("Bem-vindo a Calculadora Básica!")
var_números1 = int(input("Digite o primeiro valor:"))
var_operações = (input("Digite uma das operações(+ ,- ,* ou /):"))
var_números2 = int(input("Digite o segundo valor:"))

if var_operações == "+":
   print(f"A soma entre {var_números1} e {var_números2} é {var_números1 + var_números2}!")

elif var_operações == "-":
   print(f"A subtração entre {var_números1} e {var_números2} é {var_números1 - var_números2}!")

elif var_operações == "*":
    print(f"A multiplicação entre {var_números1} e {var_números2} é {var_números1 * var_números2}!")

elif var_operações == "/":
   
    if var_números2 != 0:
        print(f"A divisão entre {var_números1} e {var_números2} é {var_números1 / var_números2:.2f}!")
    else:
        print("Oooops! O número que você tentou dividir não existe!")

else:
    print("Oooops! Não entendo o que você quer calcular!")