from easygui import *
import sys
import sqlite3

while 1:
    buttonbox('What do you want to do?', 'Choose what to do', ('Stocktake',\
                                                               'Edit your bar'))
    conn = sqlite3.connect('mybar.db')
    c = conn.cursor()

    n_and_ids = {}
    title = 'Stocktake'
    msg = 'Select which bottle you would like to measure'
    avail_choices = c.execute('SELECT name, f_id FROM [mybar]').fetchall()
    choices = [avail_choices[x][0] for x in range(len(avail_choices))]
    for tup in avail_choices:
        n_and_ids[tup[0]] = tup[1]
    choice = choicebox(msg, title, choices)
    print("Selected {}".format(choice))

    
    while True:
        msg = 'Enter the weight of the bottle'
        current_weight = enterbox(msg)
        try:
            current_weight = float(current_weight)
            break
        except:
            msgbox('Please try entering just a number. eg, 1.246')
    print("Current weight of " + str(current_weight))
    empty_weight = c.execute('SELECT bottle_weight_empty from mybar WHERE f_id =?;',(n_and_ids[choice],)).fetchone()
    print("This has the id of {}".format(n_and_ids[choice]))
    
    if empty_weight[0] == '':
        full_weight = c.execute('SELECT bottle_weight_full from mybar WHERE f_id =?;',(n_and_ids[choice],)).fetchone()
        full_weight = full_weight[0]
        empty_weight = full_weight-(0.9201*.75)
        print(full_weight)
        print("changing it")
        print(empty_weight)
    else:
        empty_weight = float(empty_weight[0])
        print("Empty weight of {}".format(empty_weight))
        
    remaining_liquor = round(((current_weight - empty_weight)/0.9501),2)
    msgbox('The remaining alcohol left in the bottle is {} litres, or {} shots.'.format(remaining_liquor,round((remaining_liquor/0.03),2)))
