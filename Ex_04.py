#4.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido (Utilize elif).

letra=str(input("Digite (F)-feminino, (M)-masculino: ").upper())

if letra == "M":
    print("M - Masculino")
elif letra == "F":
    print("F - Feminino")
else:
    print("Sexo invalido")