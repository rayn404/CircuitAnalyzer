resistors = [[[0,0],[2,2],0],
             [[2,2],[4,4],1],
             [[4,4],[2,2],3],
             [[4,4],[2,2],2],
             [[4,4],[2,2],2],
             [[4,4],[6,6],1]]

nodes = []
def node_find(new_resistors, change=False):
    new_nodes = []
    for i in range(len(new_resistors)):
        if new_resistors[i][0] not in new_nodes:
            new_nodes.append(new_resistors[i][0])
        if new_resistors[i][1] not in new_nodes:
            new_nodes.append(new_resistors[i][1])

        indices = new_nodes.index(new_resistors[i][0]), new_nodes.index(new_resistors[i][1])
        if indices[0]>indices[1]:
            indices=indices[::-1]
        new_resistors[i][0], new_resistors[i][1] = indices

    if change:
        global nodes, resistors
        nodes, resistors= new_nodes, new_resistors
    return new_nodes, new_resistors

def ptp(new_res, change=False):
    for i in new_res:
        if i[0]==i[1]:
            new_res.remove(i)
    if change:
        global resistors
        resistors=new_res
    return new_res

def parallel(new_resistors, change=False):
    parallel = dict()
    for i in range(len(new_resistors)-1):
        for j in range(i+1, len(new_resistors)):
            if new_resistors[i][0:2] == new_resistors[j][0:2]:
                tup_conn = tuple(new_resistors[i][0:2])
                if tup_conn in parallel:
                    if parallel[tup_conn][0]==i:
                        parallel[tup_conn].append(j)
                else:
                    parallel[tup_conn] = [i, j]
    for node,res in parallel.items():
        r, free = 0, False
        for i in res[::-1]:
            i_res = new_resistors[i][2]
            if i_res==0:
                r=0
                free=True
            if not free:
                r+=1/i_res
            new_resistors.pop(i)
        r = r and 1/r
        new_resistors.append(list(node)+[r])
    
    if change:
        global resistors
        resistors=new_resistors
        
    return parallel, new_resistors

def series(new_res, change=False):
    node_count = dict()
    temp = []
    series = []
    for i,j,r in new_res:
        node_count[i], node_count[j] = node_count.get(i, 0)+1, node_count.get(j, 0)+1
    for r in range(len(new_res)):
        if ((node_count[new_res[r][0]]==2 + node_count[new_res[r][1]]==2)>=1):
            for j in range(len(series)):
                comb_sorted = sorted(series[j][0:2]+new_res[r][0:2])
                if (len(set(comb_sorted[0:2]))==1 + len(set(comb_sorted[0:2]))==1 + len(set(comb_sorted[0:2]))==1)==1:
                    temp.extend([r,j])
                    if comb_sorted[1]==comb_sorted[0]:
                        series.append()
            else:
                temp.append(new_res[r])
                series.append([new_res[r]])
    print(series) 
            

print(node_find(resistors, True))
print(parallel(resistors, True))
print(series(resistors, True))