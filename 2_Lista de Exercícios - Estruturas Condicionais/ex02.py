a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

if a < b and a < c:
    print("a é o menor numero")
elif b < a and b < c:
    print("b é o menor numero")
else:
    print("c é o menor numero")
