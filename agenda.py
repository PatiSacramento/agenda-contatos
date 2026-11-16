AGENDA = {}

AGENDA["Patricia"] = {
    "telefone":"99999-9999",
    "email": "patricia@email.com",
    "endereco": "av. 1",    
}

AGENDA["Iago"] = {
    "telefone":"99999-8888",
    "email": "iago@email.com",
    "endereco": "av. 1",    
}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print("Agenda vazia")
        

def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:",AGENDA[contato]["telefone"]) 
        print("E-mail:",AGENDA[contato]["email"]) 
        print("Endereço:",AGENDA[contato]["endereco"]) 
        print("___________________")
    except KeyError:
        print("Contato inexistente")
    except Exception as error:
        print("Um erro inesperado ocorreu.")
        print(error)


def incluir_editar_contato(contato ):
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    endereco = input("Digite o endereco do contato: ")

    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print("Contato {} adicionado/editado com sucesso!".format(contato))
    print("___________________")
    mostrar_contatos()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print("Contato {} removido com sucesso!".format(contato))
        print("___________________")
        mostrar_contatos()
    except KeyError:
        print("Contato inexistente")
    except Exception as error:
        print("Um erro inesperado ocorreu.")
        print(error)
    

def imprimir_menu():
    print()
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - Fechar agenda")
    print("___________________")


while True:
    imprimir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_contatos()
    elif opcao == "2":
        contato = input("Digite o nome do contato: ")
        buscar_contato(contato)
    elif opcao == "3":
        contato = input("Digite o nome do contato: ")
        try: 
            AGENDA[contato]
            print("Contato já existe")
            continue
        except:
            incluir_editar_contato(contato)
    elif opcao == "4":
        contato = input("Digite o nome do contato: ")
        try: 
            AGENDA[contato]
            print("Editando contato:", contato)
            incluir_editar_contato(contato)
        except:
            print("Contato inexistente")
           
    elif opcao == "5":
        contato = input("Digite o nome do contato a ser deletado: ")
        excluir_contato(contato)
    elif opcao == "0":
        break
    else:
        print("Opção inválida")