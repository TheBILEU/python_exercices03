# Escreva um programa em Python que lê uma sequência de 10 números reais e imprime qual o
# maior e qual o menor valor dessa sequência.

num1 = float(input("Digite o 1° número: "))
maior = num1
menor = num1

for i in range(2, 11):
  num1 = float(input(f"Digite o {i}° número: "))
  
  if (num1 < menor):
    menor = num1
  if (num1 > maior):
    maior = num1
    
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
