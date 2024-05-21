# Escreva um programa em Python que leia as 10 notas de uma avaliação dos alunos que
# cursam uma disciplina de algoritmos, calcule e imprima na tela (nesta ordem):
# A quantidade de notas maiores ou iguais a 7;
# A quantidade de notas maiores ou iguais a 3 e menores que 7;
# A quantidade de notas menores que 3;
# A média da turma na avaliação.


notas = float(input('Digite a nota do 1º aluno: '))
media = 0
sum = notas

countNotasPositivas = 0
if (notas >= 7):
  countNotasPositivas += 1
  
countNotas = 0
if (notas >= 3) and (notas < 7):
  countNotas += 1

countNotasNegativas = 0
if (notas < 3):
  countNotasNegativas += 1

for i in range(2, 11):
  notas = float(input(f'Digite a nota do {i}º aluno: '))
  sum += notas
  media = sum / 10
  if (notas >= 7):
    countNotasPositivas += 1
  if (notas >= 3) and (notas < 7):
    countNotas += 1
  if (notas < 3):
    countNotasNegativas += 1

print(f"A quantidade notas maiores que 7 (ou igual): {countNotasPositivas}")
print(f"A quantidade notas entre 3 e 7: {countNotas}")
print(f"A quantidade de notas menores que 3: {countNotasNegativas}")
print(f"A média da turma na avaliação: {media}")