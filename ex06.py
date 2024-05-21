# Escreva um programa em Python que imprime todos os números primos entre 1 e n (n
# incluso), onde n é fornecido pelo usuário.

# Números primos entre 1 e 50
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43 e 47
n = int(input('Digite um número natural: '))

for num in range(2, n + 1):
  primo = True 
  for i in range(2, int(num **0.5) + 1):
    if num % i == 0:
      primo = False
      break
  if primo:
    print(num, end="  ")
