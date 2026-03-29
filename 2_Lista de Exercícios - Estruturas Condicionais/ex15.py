n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print(f"\nMédia final: {media:.2f}")

if media < 3.0:
    print("Conceito: Reprovado")
elif media < 7.0:
    print("Conceito: Exame")
    exame = 18.0 - (n1 + n2 + n3)
    print(f"Você precisa tirar no mínimo {exame:.2f} no exame para ser aprovado.")
else:
    print("Conceito: Aprovado")
    
#na minha cabeca é necessario ficar com 18 pontos somando a n1, n2 e n3 entao a nota minima seria 18 - (somatorio das notas)