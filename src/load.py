import sqlite3
import os
from pymongo import MongoClient

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

    def load_data_atlas(self, universities, db_name, collection_name):
        """Carrega dados no MongoDB Atlas."""
        client = None
        try:
            # Pega a connection string do .env
            mongodb_uri = os.getenv('MONGODB_URI')
            if not mongodb_uri:
                raise ValueError("MONGODB_URI não encontrada no arquivo .env")
            
            client = MongoClient(mongodb_uri)
            db = client[db_name]
            collection = db[collection_name]
            
            # Limpa a coleção antes de inserir novos dados
            collection.delete_many({})
            
            # Insere os dados
            if universities:
                collection.insert_many(universities)
                print(f"{len(universities)} registros inseridos no MongoDB.")
            else:
                print("Nenhum dado para inserir.")
                
        except Exception as e:
            print(f"Erro ao inserir dados no MongoDB: {e}")
        finally:
            if client:
                client.close()