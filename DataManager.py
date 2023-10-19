import os
import sqlite3
from datetime import datetime

def con_cur():
    con=sqlite3.connect("CubeBase.db")
    cur=con.cursor()
    return con,cur

con, cur = con_cur() #initialize connection and cursor only once to save time
#use global con, cur everywhere else
#this introduces an issue, cursor must be closed at the end and committed

def create_tables():
    global con, cur
    
    query = '''CREATE TABLE IF NOT EXISTS OpenTable(
        STATE CHAR(54) PRIMARY KEY,
        R CHAR(54),
        RC CHAR(54),
        L CHAR(54),
        LC CHAR(54),
        U CHAR(54),
        UC CHAR(54),
        F CHAR(54),
        FC CHAR(54),
        D CHAR(54),
        DC CHAR(54),
        B CHAR(54),
        BC CHAR(54),
        HUE TINYINT
    )'''
    
    cur.execute(query)
    
    query = '''CREATE TABLE IF NOT EXISTS CloseTable(
        STATE CHAR(54) PRIMARY KEY,
        R CHAR(54),
        RC CHAR(54),
        L CHAR(54),
        LC CHAR(54),
        U CHAR(54),
        UC CHAR(54),
        F CHAR(54),
        FC CHAR(54),
        D CHAR(54),
        DC CHAR(54),
        B CHAR(54),
        BC CHAR(54),
        HUE TINYINT
    );'''
    
    cur.execute(query)
    
    con.commit()

def insert_open(state,HUE,R=None,RC=None,L=None,LC=None,U=None,UC=None,F=None,FC=None,D=None,DC=None,B=None,BC=None):
    global con, cur
    cur.execute('INSERT INTO OpenTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(state,R,RC,L,LC,U,UC,F,FC,D,DC,B,BC,HUE))
    con.commit()

def insert_close(state,R,RC,L,LC,U,UC,F,FC,D,DC,B,BC,HUE):
    global con, cur
    cur.execute('INSERT INTO CloseTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(state,R,RC,L,LC,U,UC,F,FC,D,DC,B,BC,HUE))
    con.commit()

def first_row():
    global con, cur
    cur.execute('SELECT * FROM OpenTable LIMIT 1;')
    process_node = cur.fetchone()
    #print('Processing node: ',process_node)
    return process_node

'''def last_row_open():
    global con, cur
    cur.execute('SELECT ID FROM OpenTable ORDER BY ID DESC LIMIT 1;')
    lastid = cur.fetchone()
    #print('Open last ID',lastid)
    return lastid

def last_row_close():
    global con, cur
    cur.execute('SELECT ID FROM CloseTable ORDER BY ID DESC LIMIT 1;')
    lastid = cur.fetchone()
    print('Close last ID',lastid)
    return lastid'''

def searchstate(state):
    global con, cur
    cur.execute('SELECT * FROM OpenTable WHERE STATE = ?',(state,))
    id = cur.fetchall()
    if len(id) > 1:
        return None
    return len(id) == 1

def update_record(STATE,R=None,RC=None,L=None,LC=None,U=None,UC=None,F=None,FC=None,D=None,DC=None,B=None,BC=None):
    global con, cur
    update_query = """
        UPDATE OpenTable
        SET
            R = CASE WHEN ? IS NOT NULL THEN ? ELSE R END,
            RC = CASE WHEN ? IS NOT NULL THEN ? ELSE RC END,
            L = CASE WHEN ? IS NOT NULL THEN ? ELSE L END,
            LC = CASE WHEN ? IS NOT NULL THEN ? ELSE LC END,
            U = CASE WHEN ? IS NOT NULL THEN ? ELSE U END,
            UC = CASE WHEN ? IS NOT NULL THEN ? ELSE UC END,
            F = CASE WHEN ? IS NOT NULL THEN ? ELSE F END,
            FC = CASE WHEN ? IS NOT NULL THEN ? ELSE FC END,
            D = CASE WHEN ? IS NOT NULL THEN ? ELSE D END,
            DC = CASE WHEN ? IS NOT NULL THEN ? ELSE DC END,
            B = CASE WHEN ? IS NOT NULL THEN ? ELSE B END,
            BC = CASE WHEN ? IS NOT NULL THEN ? ELSE BC END
        WHERE STATE = ?;
    """
    cur.execute(update_query,(R,R,RC,RC,L,L,LC,LC,U,U,UC,UC,F,F,FC,FC,D,D,DC,DC,B,B,BC,BC,STATE))
    con.commit()

def delete_open_single(state):
    global con, cur
    cur.execute('DELETE FROM OpenTable WHERE STATE = ?',(state,))
    con.commit()

def printallopen():
    global con, cur
    cur.execute('SELECT * FROM OpenTable')
    records = cur.fetchall()
    return records

def printallclose():
    global con, cur
    cur.execute('SELECT * FROM CloseTable')
    records = cur.fetchall()
    return records

def destroy():
    con.commit()
    cur.close()
    con.close()

def load_open():
    global con, cur
    st = datetime.now()
    con,cur = con_cur()
    cur.execute('SELECT * FROM OpenTable')
    data = cur.fetchall()
    et = datetime.now()
    print(f"Done loading {len(data)} in time: {et-st}")
    return data

def write_clt(records):
    global con, cur
    cur.executemany('INSERT INTO CloseTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',records)
    con.commit()

def select_slice(offset,limit):
    global con, cur
    query = 'SELECT * FROM OpenTable'
    if limit is not None:
        query += f' LIMIT {limit}'
    if offset is not None:
        query += f' OFFSET {offset}'
    #cur.execute(f"SELECT * FROM OpenTable {f'LIMIT {limit}' if limit != None else ''} {f'OFFSET {offset}' if offset != None};")
    cur.execute(query)
    return cur.fetchall()

def optlen():
    global con, cur
    cur.execute('SELECT COUNT(*) FROM OpenTable;')
    return cur.fetchone()[0]