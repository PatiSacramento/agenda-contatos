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
    for contato in AGENDA:
        buscar_contato(contato)

        print("___________________")


def buscar_contato(contato):
    print("Nome:", contato)
    print("Telefone:",AGENDA[contato]["telefone"]) 
    print("E-mail:",AGENDA[contato]["email"]) 
    print("Endereço:",AGENDA[contato]["endereco"]) 


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print("Contato {} adicionado com sucesso!".format(contato))
    print("___________________")
    mostrar_contatos()


#mostrar_contatos()
#buscar_contato("Patricia")
incluir_contato("Claudia", "99999-7777", "claudia@email.com", "av.2")