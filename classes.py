def incluir_classes(con, nome):
    con.execute("INSERT INTO classes(nome) VALUES(?)", (nome,))
    con.commit()

def listar_classes(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM classes")

    resultados = cursor.fethall()

    for linha in resultados:
        print(f"ID: {linha['id']}    NOME: {linha['nome']}")