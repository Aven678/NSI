import sqlite3, sys

def sql_select(val):
    connexion = sqlite3.connect('mynewbase.db')
    c = connexion.cursor()
    c.execute("SELECT Note FROM notes WHERE Nom = ?", val)
    notes = c.fetchall()
    if len(notes) == 0:
        print("Aucune note trouvée")
    print("Note : ",notes[0][0])
    connexion.close()

def sql_saisie(val):
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

def menu():
    print("Menu")
    print("1. Rentrer des notes")
    print("2. Consulter des notes")
    print("3. Quitter")
    choix = input("choix ? ")

    if choix == "1":
        saisie()
    elif choix == "2":
        consultation()
    elif choix == "3":
        sys.exit()

def saisie():
    while True:
        nom = input("Nom ? ")
        if nom in ["Q","q"]:
            break

        note = input("Note ? ")
        val = (nom, note)
        sql_saisie(val)

def consultation():
    print("Consultation des notes (tapez Q pour sortir)")
    while True:
        nom = input("Nom ? ")
        if nom in ["Q","q"]:
            break

        sql_select((nom, ))
        print("---")


while True:
    menu()
