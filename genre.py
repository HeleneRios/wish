import sqlite3

gen_name = input("Enter Genre: ").title().strip()

conn = sqlite3.connect("wish.db")

c = conn.cursor()

c.execute("insert into genres (genre) values (?)", (gen_name,))


conn.commit()
conn.close()