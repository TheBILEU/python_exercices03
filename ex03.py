n = int(input("Digite um número: "))
m = int(input('Mais um número: '))

if(m < n):
  n, m = m, n

for f in range(n, m + 1):
  celsius = (f - 32) * 5/9
  print(f"F: {f}°       C: {celsius:.1f}°")
