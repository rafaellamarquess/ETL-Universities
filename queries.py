import sqlite3

con = sqlite3.connect("universidades.db")
cur = con.cursor()

print("\n1️⃣ Total de universidades por país:")
for row in cur.execute("SELECT country, COUNT(*) FROM universities GROUP BY country;"):
    print(row)

print("\n2️⃣ Universidades de um país específico (ex: Brazil):")
for row in cur.execute("SELECT name FROM universities WHERE country = 'Brazil' LIMIT 10;"):
    print(row)

print("\n3️⃣ Busca por nomes contendo 'Technology':")
for row in cur.execute("SELECT name, country FROM universities WHERE name LIKE '%Technology%' LIMIT 10;"):
    print(row)

con.close()
