def incluir_inventario(con, personagem_id, item_id, quantidade):
    con.execute("INSERT INTO inventario(nome, tipo, poder) VALUES(?, ?, ?)", (personagem_id, item_id, quantidade,))
    con.commit

def listar_inventario(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM inventario")

    resultados = cursor.fethall()

    for linha in resultados:
        print(f"ID: {linha['id']}    ID DO JOGADOR: {linha['personagem_id']}    ID DO ITEM: {linha['item_id']}    QUANTIDADE: {linha['quantidade']}")