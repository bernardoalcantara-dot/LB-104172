import os
os.system("cls")

num = int(input("digite um numero: "))
mun = int(input("digite outro numero: "))
nun = int(input("digite mais outro numero: "))

maior = max(num, mun, nun)
menor = (num, mun, nun)

print(f" os numeros sao {num}, {mun} e {nun}")
print(f"o maior é: ", maior)
print("o menor é: ", menor)