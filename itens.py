def incluir_itens(con, nome, tipo, poder):
    con.execute("INSERT INTO itens(nome, tipo, poder) VALUES(?, ?, ?)", (nome, tipo, poder,))
    con.commit

def listar_itens(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM itens")

    resultados = cursor.fethall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}    TIPO: {linha['tipo']}    PODER: {linha['poder']}")

def get_id_autor(con, nome_item):
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM itens WHERE nome = '{nome_item}'")
    resultado = cursor.fetchone()
    return resultado[0]