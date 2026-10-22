# RPG_python-bd


Completar o sistema de cadastro de um jogo de RPG escrito em Python. Ele guarda
jogadores, personagens, classes, itens e o inventário de cada personagem em um banco de dados.
Você vai aprender a criar uma conexão com o banco, incluir registros, buscar por id e por nome e listar
tudo usando comandos SQL.

**Arquivos:**  
*  **main.py:** programa principal, menu e conexão com o banco  
*  **rpg.py:** cria o arquivo rpg.db e as 5 tabelas  
*  **classes.py:** id e nome  
*  **jogadores.py:** id, nome e apelido  
*  **itens.py:** id, nome, tipo e poder  
*  **personagens.py:** id, nome, nivel, jogador_id e classe_id  
*  **inventario.py:** id, personagem_id, item_id e quantidade 