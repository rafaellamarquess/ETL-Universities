import sqlite3


class Load():

    def _init_(self):
        pass

    def load_data(self, universities, table_name):

        # Criar o banco e se concectar nele
        con = sqlite3.connect("universidades.db")
        c = con.cursor()

        # Criar a tabela no banco
        c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}
                (
                id INTERGER PRIMARY KEY,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
                );
        ''')

        for university in universities: 
            c.execute('''INSERT INTO universities (name, country, state_province, web_pages, domains) VALUES (?,?,?,?,?);''',
                    (university.get('name'), 
                    university.get('country'), 
                    university.get('state-province'), 
                    ', '.join(university.get('web_pages', [])), 
                    ', '.join(university.get('domains', []))))

        con.commit()
        con.close()