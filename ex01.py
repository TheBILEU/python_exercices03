# Faça um programa em Python que solicite dois números naturais e exiba os múltiplos de 7
# existentes entre estes números (não inclui os números informados). Imprima os múltiplos em
# uma única linha e com 1 espaço entre eles.


num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo número: "))

if (num1 < 0) and (num2 < 0): 
  print('Apenas números naturais')
else:
  if (num1 < num2):
    for i in range(num1, num2):
      if (i % 7 == 0):
        print(i, end=" ")
  else: 
    print(f"{num1} é maior que {num2}, não é possível determinar o intervalo")