#Camada de Entidades
#Guardam as informações

class Livro:

    def __init__(self,id_livro, titulo, autor, ano, ibsn):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.ibsn = ibsn
        self.disponivel = True

class Usuario:

    def __init__(self, id_usuario, nome, email, telefone):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.telefone = telefone