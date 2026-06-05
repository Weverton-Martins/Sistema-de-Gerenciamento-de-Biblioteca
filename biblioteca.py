#Camada de Controle

#Importando os moldes do arquivo modelos.py
from modelos import Livro, Usuario
import json
import os

class GerenciadorBiblioteca:
    #Definindo os dicionarios
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = {}
        self.proximo_id_livro = 1
        self.proximo_id_usuario = 1
        self.proximo_id_emprestimo = 1
        self.carregar_dados() 

#Definindo as funções
    def cadastrar_livro(self, titulo, autor, ano,ibsn):
        id_gerado = f'LIV-{self.proximo_id_livro}'
        novo_livro = Livro(id_gerado,titulo, autor, ano, ibsn)
        self.livros[id_gerado] = novo_livro
        self.proximo_id_livro += 1
        #chamando o metodo salvar
        self.salvar_dados()

        return True

    def cadastrar_usuario(self, nome, email, telefone):
        id_gerado = f'USR-{self.proximo_id_usuario}'
        novo_usuario = Usuario(id_gerado, nome, email, telefone)
        self.usuarios[id_gerado] = novo_usuario
        self.proximo_id_usuario += 1
        self.salvar_dados()

        #Facilita na interface pro usuario saber seu ID
        return id_gerado

    def empresta_livros(self, id_usuario, id_livro):
        if id_usuario in self.usuarios and id_livro in self.livros:

            if self.livros[id_livro].disponivel == True:
                self.livros[id_livro].disponivel = False
            
                id_gerado = f'EMP-{self.proximo_id_emprestimo}'

                self.emprestimos[id_gerado] = {
                    "id_usuario": id_usuario,
                    "id_livro": id_livro,
                    "status": "Ativo"
                }

                self.proximo_id_emprestimo += 1
                self.salvar_dados()
                return True
            else:
                return False
        else:
            return False
        
    def devolucao_livros(self, id_emprestimo):
        if id_emprestimo in self.emprestimos:
            #descobre qual o livro
            id_livro_emprestado = self.emprestimos[id_emprestimo]['id_livro']
            #atribui concluido ao status do emprestimo
            self.emprestimos[id_emprestimo]['status'] = 'Concluido'
            #muda o status do livro
            self.livros[id_livro_emprestado].disponivel = True

            self.salvar_dados()
            return True
        else:
            return False
        
    def pesquisar_livro(self, termo_pesquisa):
        resultado = []

        for livro in self.livros.values():
            if termo_pesquisa.lower() in livro.titulo.lower():
                resultado.append(livro)
        
        return resultado

    def pesquisar_usuario(self, termo_pesquisa):
        resultado = []

        for usuario in self.usuarios.values():
            if termo_pesquisa.lower() in usuario.nome.lower():
                resultado.append(usuario)
        
        return resultado

    def listagem_livros(self):
        resultado = []

        for livro in self.livros.values():
            if livro.disponivel == True:
                resultado.append(livro)
        
        return resultado

    def listagem_livros_emprestados(self):
        resultado = []

        for livro in self.livros.values():
            if livro.disponivel == False:
                resultado.append(livro)
        
        return resultado

    def salvar_dados(self):

        dados_para_salvar = {
            "livros": {},
            "usuarios": {},
            "emprestimos" : self.emprestimos,
        }
        #Desencapsulando os objetos Livro para dicionários comuns
        for id_livro, obj_livro in self.livros.items():
                dados_para_salvar["livros"][id_livro] = obj_livro.__dict__
                
        #Desencapsulando os objetos Usuario para dicionários comuns
        for id_usuario, obj_usuario in self.usuarios.items():
            dados_para_salvar["usuarios"][id_usuario] = obj_usuario.__dict__
            
        # Lógica de Salvar
        with open('dados_biblioteca.json', 'w') as arquivo:
            json.dump(dados_para_salvar, arquivo, indent=4)

    def carregar_dados(self):

        if os.path.exists('dados_biblioteca.json'):
            with open('dados_biblioteca.json', 'r') as arquivo:
                dados_carregados = json.load(arquivo)

                livros_salvos = dados_carregados.get("livros", {})
                for id_livro, dados_livro in livros_salvos.items():
                    # Recria o objeto chamando a classe Livro
                    novo_livro = Livro(
                        dados_livro['id_livro'], 
                        dados_livro['titulo'], 
                        dados_livro['autor'], 
                        dados_livro['ano'], 
                        dados_livro['ibsn'] 
                    )
                    # Forçando o status de disponibilidade para ser igual ao que estava salvo
                    novo_livro.disponivel = dados_livro['disponivel']
                    
                    # Salva no dicionário da memória
                    self.livros[id_livro] = novo_livro
                
                usuarios_salvos = dados_carregados.get("usuarios", {})
                for id_usuario, dados_usuario in usuarios_salvos.items():
                    # Recria o objeto chamando a classe Usuario
                    novo_usuario = Usuario(
                        dados_usuario['id_usuario'],
                        dados_usuario['nome'],
                        dados_usuario['email'],
                        dados_usuario['telefone']
                    )
                    # Salva no dicionário da memória 
                    self.usuarios[id_usuario] = novo_usuario
                
                # RESTAURANDO OS EMPRÉSTIMOS
                self.emprestimos = dados_carregados.get("emprestimos", {})

                # A função len() conta quantos itens existem no dicionário.
                self.proximo_id_livro = len(self.livros) + 1
                self.proximo_id_usuario = len(self.usuarios) + 1
                self.proximo_id_emprestimo = len(self.emprestimos) + 1
        else:
            # Se o arquivo não existe
            # O sistema vai iniciar zerado
            pass