import os
os.system("cls")

#inicio
nota1 =float(input("nota1: "))
nota2 =float(input("nota2: "))
nota3 =float(input("nota3: "))

#processo
media = (nota1 + nota2 + nota3 ) /3
if media > 7:
    print("aluno aprovado")
else:
    print("aluno reprovado")