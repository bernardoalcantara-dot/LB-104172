import os
os.system("cls")

cart = str(input("digite seu nome: "))
idad = int(input("digite sua idade: "))
max = 65
min = 16

if idad <min:
    print("menor de idade nao elegivel ao voto")
elif idad < 17:
    print("voto opcional por menoridade")
elif idad > max:
    print("voto opcional por maioridade")
else:
    print("voto obrigatorio")