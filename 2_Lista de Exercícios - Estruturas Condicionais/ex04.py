a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

if c > a and c > b:
    print("a e b sao os menores numeros")
elif b > a and b > c:
    print("a e c sao os menores numeros")
else:
    print("b e c sao os menores numeros")