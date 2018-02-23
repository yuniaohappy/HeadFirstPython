import sqlite3

conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()
print(str(cursor.execute("""SELECT DATE('NOW')""")))
conn.commit()
conn.close()
