#3.	Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

n1=int(input("Digite um numero: "))
resto = n1 % 2

if resto == 0:
    print(n1,"e par.")
else:
    print(n1,"e impar.")