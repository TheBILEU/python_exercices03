a = int(input('Digite um número: '))
b = int(input('+1: '))
sum = 0

if a > b:
  a, b = b, a

for i in range(a, b + 1): 
  sum =  sum + i
  print(sum)


print(sum)
  