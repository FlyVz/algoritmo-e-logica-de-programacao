# a = 4


# match a:
#     case 1:
#         print("Deu 1")
#     case 3:
#         print("Deu 3")
#     case _: 
# #         print("Opcao invalida")
        
# ----------------------------------------------
        
# dia = input("Digite o dia da semana: ")

# match dia:
#     case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
#         print("Tem aula")
#     case _:
#         print("Não tem aula")

# -------------------------------------------------

num = 1

match num:
    case num if num < 0:
        print("Num é menor que zero")
    case num if num > 0:
        print("Num é maior que zero")