from ex112.biblioteca.interface import *


def arquivo_existe(nome_arquivo):
    try:
        abrir_arquivo=open(nome_arquivo,"rt")
        abrir_arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome_arquivo):
    try:
        abrir_arquivo=open(nome_arquivo,"wt+")
        abrir_arquivo.close()
    except FileNotFoundError:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome_arquivo} criado com sucesso!")


def ler_arquivo(nome_arquivo):
    try:
        abrir_arquivo=open(nome_arquivo,"rt")
    except:
        print("Erro ao ler arquivo")
    else:
        cabecalho("Pessoas cadastradas")
        for linha in abrir_arquivo:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        abrir_arquivo.close()


def cadastrar(arquivo,nome="desconhecido",idade=0):
    try:
        abrir_arquivo=open(arquivo,"at")
    except:
        print("Erro ao abrir arquivo")
    else:
        try:
            abrir_arquivo.write(f"{nome};{idade}\n")
        except:
            print("Erro ao escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado com sucesso!")
            abrir_arquivo.close()
