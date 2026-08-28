import os
from statistics import median
os.system("cls")


#ENTRADA
primeiro_numero = int(input("digite o primeiro_numero: " ))
segundo_numero = int(input("digite o segundo_numero: " ))

#PROCESSAMENTO
soma = primeiro_numero+segundo_numero
produto = primeiro_numero+segundo_numero
meida = soma /2
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

#SAIDA
print(f'\nsoma: {soma}')
print(f'produto: {produto}')
print(f'media: {median}')
