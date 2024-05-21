# Faça um programa em Python que leia 10 números reais, um de cada vez (ou seja, um por
# linha), e conte quantos são positivos, a soma dos números negativos, e a média de todos
# os valores.
# A soma dos números negativos e a média de todos os valores devem ser exibidas com
# uma casa decimal.

num = float(input('Digite o 1° número: '))
countP = 0
if (num > 0):
  countP += 1
sumNegativos = 0
if (num < 0):
  sumNegativos = num
sum = num
media = 0

for i in range(2, 11):
  num = float(input(f'Digite o {i}° número: '))
  sum += num
  media = sum / 10
  if (num < 0):
    sumNegativos += num
  if (num > 0):
    countP += 1
print(f"Soma dos números negativos: {sumNegativos:.1f}")
print(f"Foram contados {countP} números positivos")
print(f"A média de todos os valores é: {media:.1f}")