import sqlite3
import requests

# Primeiro, extrair os dados da API
response = requests.get("http://universities.hipolabs.com/search?country=Brazil")
universities = response.json()

# Criar o banco e se conectar nele
con = sqlite3.connect("universidades.db")
c = con.cursor()

# Criar a tabela no banco (corrigido INTERGER para INTEGER)
c.execute('''
CREATE TABLE IF NOT EXISTS universities
          (
          id INTEGER PRIMARY KEY,
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
print(f"Inseridas {len(universities)} universidades no banco.")