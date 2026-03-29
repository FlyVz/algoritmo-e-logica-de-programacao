origem = int(input("Digite a origem: "))

match origem:
    case origem if origem == 1:
        print("Vem do Sul")
    case origem if origem == 2:
        print("Vem do Norte")
    case origem if origem == 3:
        print("Vem do Leste")
    case origem if origem == 4:
        print("Vem do Oeste")
    case origem if origem == 5 or origem == 6:
        print("Vem do Nordeste")
    case origem if origem == 7 or origem == 8 or origem == 9:
        print("Vem do Sudeste")       
    case origem if origem >= 10 and origem <= 20:
        print("Vem do Centro-Oeste")
    case origem if origem >= 21 and origem <= 30:
        print("Vem do Noroeste")
    