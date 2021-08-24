bd = {"nome":"", "cpf":"", "nascimento":""}
restart = "y"
print("SISTEMA PARA CADASTRO")

def cadastro():
    procedimento = input("Selecione o procedimento: cadastro / consulta \n")

    if procedimento == "cadastro":

        bd["nome"] = input("Insira seu nome: ")
        bd["cpf"] = input("Insira seu CPF: ")
        bd["nascimento"] = input("Insira sua data de nascimento: ")

    elif procedimento == "consulta":
        nome_consulta = input("Digite o nome da pessoa a ser consultada: \n")
        if bd["nome"] == nome_consulta:
            print(bd)
        else: print("Não encontrado.")

    else: 
        print("Procedimento não identificado.")

    restart = input("Deseja realizar outro procedimento? y/n")

cadastro()

while restart == "y":
    cadastro()

print("Programa finalizado!")