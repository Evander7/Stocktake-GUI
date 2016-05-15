import sqlite3

conn = sqlite3.connect('liquor.db')
c=conn.cursor()
with_data = c.execute("SELECT id, (brand || ' ' || Alt_name || ' ' ||Type_of_Aged), Bottle_weight_empty, Bottle_weight_full FROM liquor WHERE Bottle_weight_empty or Bottle_weight_full >0;").fetchall()
print(with_data)

conn2 = sqlite3.connect('mybar.db')
c2 = conn2.cursor()

for tup in with_data:
    _id = tup[0]
    name = tup[1]
    empty_weight = tup[2]
    full_weight = tup[3]
    print(_id,name,empty_weight,full_weight)
    c2.execute('INSERT INTO mybar (f_id, name, bottle_weight_empty, bottle_weight_full) VALUES (?,?,?,?);', (_id, name, empty_weight, full_weight))

    conn2.commit()
    
