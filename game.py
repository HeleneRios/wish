import sqlite3

game_name = input("Enter Game: ").title().strip()
genres = input("Enter list of genres. Use spaces: ")
publisher = input("Enter Publisher: ").title().strip()
main_hours = int(input("Enter the number of hours (Main): "))
side_hours = int(input("Enter the number of hours (Side): "))
lowest_price = int(input("Enter the lowest recorded price: "))
buy_at = int(input("Enter suggested buying price: "))
rating = input("Enter rating: ").title().strip()
notes = input("Notes: ")

genre_list = genres.split()

conn = sqlite3.connect("wish.db")

c = conn.cursor()

c.execute("select publisher_id from publishers where name = ?", (publisher,))
pub_fetched = c.fetchone()

if pub_fetched is None:
    c.execute("insert into publishers (name) values (?)", (publisher,))

new_pub = c.lastrowid


c.execute("insert into games (title, publisher, main_hours, side_hours, lowest_price, considered_price, rating, notes) values (?,?,?,?,?,?,?,?)", (game_name, new_pub, main_hours, side_hours, lowest_price, buy_at, rating, notes,))

conn.commit()
conn.close()