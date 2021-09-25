#7.	Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

n1=int(input("Digite um numero de 1 a 7: "))

if n1 == 1:
    print("1 - Domingo")
elif n1 == 2:
    print("2 - segunda")
elif n1 == 3:
    print("3 - terça")
elif n1 == 4:
    print("4 - quarta")
elif n1 == 5:
    print("5 - quinta")
elif n1 == 6:
    print("6 - sexta")
elif n1 == 7:
    print("7 - sabado")
else:
    print("Valor invalido")