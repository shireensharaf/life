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

