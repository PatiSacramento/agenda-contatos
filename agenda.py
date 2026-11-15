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
        print("Nome:", contato)
        print("Telefone:",AGENDA[contato]["telefone"]) 
        print("E-mail:",AGENDA[contato]["email"]) 
        print("Endereço:",AGENDA[contato]["endereco"]) 

        print("___________________")


def buscar_contato(contato):
    print("Nome:", contato)
    print("Telefone:",AGENDA[contato]["telefone"]) 
    print("E-mail:",AGENDA[contato]["email"]) 
    print("Endereço:",AGENDA[contato]["endereco"]) 


#mostrar_contatos()
buscar_contato("Patricia")