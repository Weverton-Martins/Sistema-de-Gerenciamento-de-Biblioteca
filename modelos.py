#Camada de Entidades
'''
AQUI ONDE FICA OS DADOS E MODELOS
'''
#Guardam as informações da classe livro
class Livro:

    def __init__(self,id_livro, titulo, autor, ano, ibsn):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.ibsn = ibsn
        self.disponivel = True

#Guardam as informações da classe usuario
class Usuario:

    def __init__(self, id_usuario, nome, email, telefone):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.telefone = telefone