salario = float(input("Qual seu salário: "))
despesas = input("Você tem contas para pagar este mês? Digite SIM ou NÃO").lower()

sum = 0

if (despesas == 'sim'):
  qtdContas = int(input("Quantas contas você deseja pagar: "))
  for i in range(1, qtdContas + 1):
   precoConta = float(input(f"Digite o valor da {i} conta:"))
   sum += precoConta
   if (sum > salario):
     print(f"Você precisa reduzir suas despesas em R${sum} reais")
   elif (salario - sum < salario):
     print(f"Parabéns! Este mês você economizou R${salario - sum} reais")





