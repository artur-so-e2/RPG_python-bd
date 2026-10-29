def incluir_jogadores(con, nome, apelido):
    con.execute("INSERT INTO jogadores(nome, apelido) VALUES(?, ?)", (nome, apelido,))
    con.commit()

def listar_jogadores(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM jogadores")

    resultados = cursor.fethall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}    APELIDO: {linha['apelido']}")

def get_id_autor(con, nome_personagem):
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM jogadores WHERE nome = '{nome_personagem}'")
    resultado = cursor.fetchone()
    return resultado[0]