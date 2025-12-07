import sqlite3

pub_name = input("Enter Publisher Name: ").title().strip()

conn = sqlite3.connect("wish.db")

c = conn.cursor()

c.execute("insert into (name) values (?)", (pub_name,))


conn.commit()
conn.close()