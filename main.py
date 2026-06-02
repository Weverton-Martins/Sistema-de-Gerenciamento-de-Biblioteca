#Sistema de Gerenciamento de Biblioteca que permite:
'''● Cadastrar novos livros e usuários.
● Emprestar e devolver livros.
● Pesquisar livros e usuários.
● Listar livros disponíveis e emprestados.
● Gerar relatórios de empréstimos.
● Persistir dados em arquivos para garantir que as informações sejam mantidas entre
as execuções do programa.
● Testar funcionalidades para garantir a confiabilidade do sistema.'''

import json
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
