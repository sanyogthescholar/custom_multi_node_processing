import DataManager as dm
from datetime import datetime
from logic import calculate

def printall():
    print('OpenTable:\n')
    for i in dm.printallopen():
        print(i)
    #print(dm.printallopen(),'\n')
    print('CloseTable:\n')
    for i in dm.printallclose():
        print(i)
    #print(dm.printallclose())

def resettables():
    con,cur = dm.con_cur()
    cur.execute('DELETE FROM OpenTable')
    cur.execute('DELETE FROM CloseTable')
    con.commit()
    #cu = structure.Cube(["O","O","O","O","O","O","O","O","O","G","G","G","W","W","W","B","B","B","Y","Y","Y","G","G","G","W","W","W","B","B","B","Y","Y","Y","G","G","G","W","W","W","B","B","B","Y","Y","Y","R","R","R","R","R","R","R","R","R"])
    #st = structure.list_to_string(cu.state)
    st = "OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR"
    dm.insert_open(st,0)
    cur.close()
    con.close()

def load_open():
    st = datetime.now()
    con,cur = dm.con_cur()
    cur.execute('SELECT * FROM OpenTable')
    data = cur.fetchall()
    et = datetime.now()
    cur.close()
    con.close()
    print("Done:\t",et-st,data)

#con, cur = dm.con_cur()
calculate([1,0])
printall()
#resettables()
#load_open()
#dm.create_tables()
#print(dm.printallclose())
#input()
dm.destroy()
print('Success!')