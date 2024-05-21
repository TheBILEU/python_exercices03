# Calcule a parte inteira da raiz quadrada de um número inteiro positivo sem usar a função sqrt.
# Para isso, você precisa saber que a raiz quadrada de um número n é igual aproximadamente
# à quantidade de números ímpares consecutivos (a partir do 1) cuja soma é igual a n (ou o
# mais próxima possível de n).

n = int(input("Digite um número que deseja encontrar a raiz: "))

raizQuadrada = 0
somaImpar = 0

for i in range(1, n + 1, 2):
  if i % 2 != 0:
    raizQuadrada += 1
    somaImpar += i
    if somaImpar >= n:
      break

print(f"A raiz quadrada de {n} é: {raizQuadrada}")