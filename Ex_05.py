#5.	Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#o	A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
#o	A mensagem "Reprovado", se a média for menor do que seis;
#o	A mensagem "Aprovado com Distinção", se a média for igual a dez.


n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 6 and media < 10:
    print("Aprovado")
elif media >= 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")


