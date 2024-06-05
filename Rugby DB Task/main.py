import sqlite3

# Connect to the database
db = sqlite3.connect('rugby.db')
c = db.cursor()
sql = "SELECT * FROM player"
c.execute(sql)
results = c.fetchall()
print(results)
db.close()