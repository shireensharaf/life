def grid_view(rows,cols, l):
    col_count = 0
    l2 =[]
    for i in range(0,rows):
        l1 = []
        for j in range(0, cols):
            if(col_count in l):
                l1.append(True)
            else:
                l1.append(False)
            col_count += 1
        l2.append(l1)
    return l2


def neighbours(l):
    return 0
