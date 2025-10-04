import sqlite3

class Load:
    def __init__(self, db_name="universidades.db"):
        self.db_name = db_name

    def create_table(self):
        """Cria a tabela de universidades no banco SQLite."""
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS universities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
            );
        ''')
        con.commit()
        con.close()

    def load_data(self, df):
        """Insere os dados tratados no banco."""
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        for _, row in df.iterrows():
            cur.execute('''
                INSERT INTO universities (name, country, state_province, web_pages, domains)
                VALUES (?, ?, ?, ?, ?);
            ''', (
                row["name"],
                row["country"],
                row["state-province"],
                row["web_pages"],
                row["domains"]
            ))

        con.commit()
        con.close()
        print("Dados inseridos no banco com sucesso.")
