
import sqlite3

database_filename = 'chinook.db'
connection = sqlite3.connect(database_filename)

cursor = connection.cursor()
cursor.execute("SELECT * FROM albums")


print(cursor.fetchone())
