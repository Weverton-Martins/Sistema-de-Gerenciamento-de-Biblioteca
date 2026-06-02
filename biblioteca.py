#Camada de Controle

#Importando os moldes do arquivo modelos.py
from modelos import Livro, Usuario

class GerenciadorBiblioteca:
    #Definindo os dicionarios
    def __init__(self):
        self.livros = {}
        self.usuario= {}
        self.emprestimo = {}
        self.proximo_id_livro = 1
        self.proximo_id_usuario = 1

#definindo as funções
def cadastrar_livro(self, titulo, autor, ano,ibsn):
    id_gerado = f'LIV-{self.proximo_id_livro}'
    novo_livro = Livro(id_gerado,titulo, autor, ano, ibsn)
    self.livros[id_gerado] = novo_livro
    self.proximo_id_livro += 1

def cadastrar_usuario(self, nome, email, telefone):
    id_gerado = f'USR-{self.proximo_id_usuario}'
    novo_usuario = Usuario(id_gerado, nome, email, telefone)
    self.usuario[id_gerado] = novo_usuario
    self.proximo_id_usuario += 1