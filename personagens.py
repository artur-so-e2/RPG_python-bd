def incluir_personagens(con, nome, nivel, jogador_id, classe_id):
    con.execute("INSERT INTO personagens(nome, nivel, jogador_id, classe_id) VALUES(?, ?, ?, ?,)", (nome, nivel, jogador_id, classe_id,))
    con.commit

def listar_personagens(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM personagens")

    resultados = cursor.fethall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}    NÍVEL: {linha['nivel']}    ID DO JOGADOR: {linha['jogador_id']}    ID DA CLASSE: {linha['classe_id']}")

def get_id_autor(con, nome_personagem):
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM personagens WHERE nome = '{nome_personagem}'")
    resultado = cursor.fetchone()
    return resultado[0]