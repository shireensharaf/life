from collections import Counter
max_len = 4
def grid_view(l):
    col_count = 0
    l2 =[]
    for i in range(0, max_len):
        l1 = []
        for j in range(0, max_len):
            if(col_count in l):
                l1.append(True)
            else:
                l1.append(False)
            col_count += 1
        l2.append(l1)
    return l2

def position_true(l):
    pos = []
    for i in range(0, max_len):
        for j in range(0, max_len):
            p = []
            if(l[i][j] == True):
                p.extend([i,j])
                pos.append(p)
    return pos

def neighbours(l,i):
    t = []
    f = []
    if (i[1]-1 >= 0 and i[0]-1 >= 0):
        if( l[i[0]-1][i[1]-1] == True):
            t.append('y')
        elif (l[i[0]-1][i[1]-1] == False):
            p=[]
            p.extend([i[0]-1,i[1]-1])
            f.append(p)
        
    if (i[0]-1 >= 0):
        if(l[i[0]-1][i[1]] == True):
            t.append('y')
        elif (l[i[0]-1][i[1]] == False):
            p=[]
            p.extend([i[0]-1, i[1]])
            f.append(p)
                
    if (i[1]+1 < max_len and i[0]-1 >= 0):
        if( l[i[0]-1][i[1]+1] == True):
            t.append('y')
        elif (l[i[0]-1][i[1]+1] == False):
            p=[]
            p.extend([i[0]-1, i[1]+1])
            f.append(p)

    if (i[1]-1 >= 0):
        if( l[i[0]][i[1]-1] == True):
            t.append('y')
        elif (l[i[0]][i[1]-1] == False):
            p=[]
            p.extend([i[0], i[1]-1])
            f.append(p)
        
    if (i[1]+1 < max_len):
        if(l[i[0]][i[1]+1] == True):
            t.append('y')
        elif (l[i[0]][i[1]+1] == False):
            p=[]
            p.extend([i[0], i[1]+1])
            f.append(p)
        
    if (i[1]-1 >= 0 and i[0]+1 < max_len):
        if(l[i[0]+1][i[1]-1] == True):
            t.append('y')
        elif (l[i[0]+1][i[1]-1] == False):
            p=[]
            p.extend([i[0]+1, i[1]-1])
            f.append(p)

    if (i[0]+1 < max_len):
        if(l[i[0]+1][i[1]] == True):
            t.append('y')
        elif (l[i[0]+1][i[1]] == False):
            p=[]
            p.extend([i[0]+1, i[1]])
            f.append(p)
               
    if (i[1]+1 < max_len and i[0]+1 < max_len):
        if(l[i[0]+1][i[1]+1] == True):
            t.append('y')
        elif (l[i[0]+1][i[1]+1] == False):
            p=[]
            p.extend([i[0]+1, i[1]+1])
            f.append(p)
    
    return len(t), f


def change_status(l):
    new_l = l.copy()
    x = position_true(l)
    false_nb = []
    die = []
    for i in x:
        true_cells, false_cells = neighbours(l,i)
        if(true_cells < 2 or true_cells > 3):
            die.append(i)
        false_nb.extend(false_cells)
    for i in die:
        l[i[0]][i[1]] = False
    count = Counter([tuple(i) for i in false_nb])
    for key, value in count.items():
        if (value == 3):
           new_l[key[0]][key[1]]=True

    return new_l
    
