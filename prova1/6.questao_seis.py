nota1 = float(input("Digite sua nota:"))
nota2 = float(input("Digite sua nota:"))

media = (nota1 + nota2) /2

if media >= 6:
 print("Aluno aprovado")
elif media == 4:
 print("Aluno recuperação")
elif media <= 4:
 print("Aluno reprovado")

