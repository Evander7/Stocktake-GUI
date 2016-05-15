import sqlite3

conn = sqlite3.connect('mybar.db')
c = conn.cursor()
avail_choices = c.execute('SELECT name, f_id FROM [mybar]').fetchall()

choices = [avail_choices[x][1] for x in range(len(avail_choices))]

print(avail_choices)
print(choices)
