import sqlite3

def executeSQL(val):
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS notes(
    Nom TEXT,
    Note INT);
    """)


    c.execute('''INSERT INTO notes VALUES (?,?)''', val)
    connexion.commit()
    connexion.close()

while True:
    nom = input("Nom ? ")
    if nom in ["Q","q"]:
        break

    note = input("Note ? ")
    val = (nom, note)
    executeSQL(val)
