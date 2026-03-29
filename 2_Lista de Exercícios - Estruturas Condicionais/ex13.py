a = 0  
c = 0  
d = 0  

b = float(input("Digite o primeiro número: "))
if b > 100:
    a += 1
elif b < 17:
    c += 1
elif 17 < b < 100:
    d += 1

b = float(input("Digite o segundo número: "))
if b > 100:
    a += 1
elif b < 17:
    c += 1
elif 17 < b < 100:
    d += 1

b = float(input("Digite o terceiro número: "))
if b > 100:
    a += 1
elif b < 17:
    c += 1
elif 17 < b < 100:
    d += 1

b = float(input("Digite o quarto número: "))
if b > 100:
    a += 1
elif b < 17:
    c += 1
elif 17 < b < 100:
    d += 1

b = float(input("Digite o quinto número: "))
if b > 100:
    a += 1
elif b < 17:
    c += 1
elif 17 < b < 100:
    d += 1

print("-" * 35)
print(f"maiores que 100: {a}")
print(f"menores que 17: {c}")
print(f"entre 17 e 100: {d}")