import sqlite3 as sqlite
from util import limpa_tela

conn = sqlite.connect('rpg.bd')
conn.row_factory = sqlite.Row