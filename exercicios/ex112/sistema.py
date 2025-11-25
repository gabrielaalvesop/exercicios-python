from ex112.biblioteca.interface import *
from ex112.biblioteca.arquivo import *
from time import sleep

arquivo = "Curso em Vídeo.txt"

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta=menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar conteúdo de um arquivo!
        ler_arquivo(arquivo)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa
        cabecalho("Novo Cadastro")
        nome=str(input("Nome: "))
        idade=int(input("Idade: "))
        cadastrar(arquivo,nome,idade)

    elif resposta == 3:
        #Opção de sair do sistema
        cabecalho("Saindo do sistema...")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)