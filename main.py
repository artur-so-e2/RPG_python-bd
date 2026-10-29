import sqlite3 as sqlite
from util import limpa_tela
from classes import incluir_classes, listar_classes
from jogadores import incluir_jogadores, listar_jogadores
from itens import incluir_itens, listar_itens
from personagens import incluir_personagens, listar_personagens
from inventario import incluir_inventario, listar_inventario

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

def menu_itens():
    limpa_tela
    while(True):
        print("-"*10, "Menu de itens", "-"*10)
        print("1 - Adicionar item\n2 - Listar itens\n3 - Voltar para o menu principal")
        opcao = input("Digite qual opção deseja fazer em itens: ")
        if opcao == '1':
            nome = input("Digite o nome do novo item: ")
            tipo = input("Digite o tipo desse item: ") 
            poder = input("Digite o poder desse item: ")
            incluir_itens(conn, nome, tipo, poder)
        elif opcao == '2':
            listar_itens(conn)
            input("Aperte 'Enter' para continuar.")
        elif opcao == '3':
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar.")

def menu_personagens():
    limpa_tela
    while(True):
        print("-"*10, "Menu de personagens", "-"*10)
        print("1 - Adicionar personagem\n2 - Listar personagens\n3 - Voltar para o menu principal")
        opcao = input("Digite qual opção deseja fazer em itens: ")
        if opcao == '1':
            nome = input("Digite o nome do novo item: ")
            nivel = input("Digite o tipo desse item: ") 
            jogador_id = input("Digite o poder desse item: ")
            classe_id = input("Digite o poder desse item: ")
            incluir_personagens(conn, nome, nivel, jogador_id, classe_id)
        elif opcao == '2':
            listar_personagens(conn)
            input("Aperte 'Enter' para continuar.")
        elif opcao == '3':
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar.")

def menu_inventario():
    limpa_tela
    while(True):
        print("-"*10, "inventario", "-"*10)
        print("1 - Adicionar item no inventario\n2 - Listar itens no inventario\n3 - Voltar para o menu principal")
        opcao = input("Digite qual opção deseja fazer em itens: ")
        if opcao == '1':
            personagem_id = input("Digite o nome do novo item: ")
            item_id = input("Digite o tipo desse item: ") 
            quantidade = input("Digite o poder desse item: ")
            incluir_inventario(conn, personagem_id, item_id, quantidade)
        elif opcao == '2':
            listar_inventario(conn)
            input("Aperte 'Enter' para continuar.")
        elif opcao == '3':
            limpa_tela()
            break
        else:
            input("Opção inválida! Aperte 'Enter' para continuar.")