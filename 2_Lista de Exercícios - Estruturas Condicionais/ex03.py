c = int(input("Digite um valor para a: "))
d = int(input("Digite um valor para b: "))

a = c
b = d

c = int(input("Digite um valor para c: "))
d = int(input("Digite um valor para d: "))

if a < b and a < c and a < d:
    print("a é o menor numero")
elif b < a and b < c and b < d:
    print("b é o menor numero")
elif c < a and c < b and c < d:
    print("c é o menor numero")
else:
    print("d é o menor numero")

