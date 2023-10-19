import structure
import DataManager as dm

#def calculate(data):
#    return sum(range(1, data + 1))

def calculate(data):
    #access the database
    con, cur = dm.con_cur()
    #data[0] = Number of records to be processed by the client
    #data[1] = Slot given to the client
    rec = data[0]
    slot = data[1]
    #Check data exists?
    #data[0] = Number of records to be processed by the client
    #data[1] = Slot given to the client
    start_record = (data[0] * data[1])
    lim = data[0]
    if start_record + data[0] > dm.optlen():
        lim = None
    if start_record < 1:
        start_record = None
    process_nodes = dm.select_slice(start_record,lim)
    process_nodes = [list(x) for x in process_nodes]
    #print(process_nodes)
    #load OpenTable
    clt = []
    opt = dm.load_open()
    opt = [list(x)+[0] for x in opt]
    dopt = {x[0]:x[1:] for x in opt}
    #print(dopt)
    states = ["R","R'","L","L'","U","U'","F","F'","D","D'","B","B'"]
    for record in process_nodes:
        state = record[0]
        for turn in range(12):
            if record[turn+1] == None:
                node = structure.Cube(structure.string_to_list(state))
                node.move(states[turn])
                strstate = structure.list_to_string(node.state)
                exi_rec = dopt.get(strstate)
                if exi_rec != None:
                    #strstate exists
                    #update record
                    if turn % 2 == 0:
                        dopt[strstate][turn+1] = state
                    else:
                        dopt[strstate][turn-1] = state
                    dopt[state][turn] = exi_rec
                    dopt[state][12] = 1
                else:
                    #Not exists
                    #Append record
                    li = [None for _ in range(12)]
                    li.append(record[13]+1)
                    li.append(2)
                    dopt[strstate] = li
        clt.append(record)
        del(dopt[state])
    #write db
    dm.write_clt(clt)
    for state in clt:
        dm.delete_open_single(state[0])
    for state in dopt.keys():
        val = dopt.get(state)
        rec = [state] + val
        #print(rec)
        if rec[-1] == 1:
            #update
            dm.update_record(rec[0],R=rec[1],RC=rec[2],L=rec[3],LC=rec[4],U=rec[5],UC=rec[6],F=rec[7],FC=rec[8],D=rec[9],DC=rec[10],B=rec[11],BC=rec[12])
        if rec[-1] == 2:
            #append
            dm.insert_open(rec[0],rec[13],R=rec[1],RC=rec[2],L=rec[3],LC=rec[4],U=rec[5],UC=rec[6],F=rec[7],FC=rec[8],D=rec[9],DC=rec[10],B=rec[11],BC=rec[12])