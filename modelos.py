#Camada de Entidades
#Guardam as informações

class Livro:

    def __init__(self,titulo, autor, ano, ibsn):
        # self.ID = ID
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.IBSN = ibsn
        self.disponivel = True

class Usuario:

    def __init__(self, nome, email, telefone):
        # self.ID = ID
        self.nome = nome
        self.email = email
        self.telefone = telefone