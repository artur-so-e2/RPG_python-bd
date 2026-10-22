import sqlite3 as sqlite
from util import limpa_tela
from classes import incluir_classes, listar_classes
from jogadores import incluir_jogadores, listar_jogadores

conn = sqlite.connect('rpg.bd')
conn.row_factory = sqlite.Row

def menu_classes():
    limpa_tela()
    while(True):
        print("-"*10, "Menu de classes", "-"*10)
        print("1 - Adicionar classe\n2 - Listar classes\n3 - Voltar para o menu principal")
        opcao = input("Digite qual opção deseja fazer em classes: ")
        if opcao == '1':
            nome = input("Digite o nome da nova classe: ")
            incluir_classes(conn, nome)
        elif opcao == '2':
            listar_classes(conn)
            input("Aperte 'Enter' para continuar.")
        elif opcao == '3':
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar.")

def menu_jogadores():
    limpa_tela()
    while(True):
        print("-"*10, "Menu de jogadores", "-"*10)
        print("1 - Adicionar classe\n2 - Listar classes\n3 - Voltar para o menu principal")
        opcao = input("Digite qual opção deseja fazer em jogadores: ")
        if opcao == '1':
            nome = input("Digite o nome do novo jogador: ")
            apelido = input("Digite o seu apelido (nick): ")
            incluir_jogadores(conn, nome, apelido)
        elif opcao == '2':
            listar_jogadores(conn)
            input("Aperte 'Enter' para continuar.")
        elif opcao == '3':
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar.")