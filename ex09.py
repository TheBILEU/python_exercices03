# Escreva um programa em Python que leia a média parcial de 10 alunos, e escreva na tela a
# situação de cada um. “APROVADO” se NF >= 7; “FINAL” se 3 <= NF < 7; “REPROVADO” se
# NF < 3.

for i in range(1, 10 + 1):
  notaFinal = float(input(f'Digite a média do {i}° aluno: '))
  if (notaFinal > 10) or (notaFinal < 0):
    print("Nota inválida... reinicie o programa")
    exit()
  else:
    if (notaFinal >= 7):
      print('APROVADO')
      print()
    if (3 <= notaFinal < 7):
      print('FINAL')
      print()
    if (notaFinal < 3):
      print('REPROVADO')
      print()