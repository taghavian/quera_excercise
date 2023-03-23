def adjacency(dim,pos):
    adj=[]
    I=[-1,0,1]
    J=[-1,0,1]
    for i in I:
        for j in J:
            if (pos[0]+i>=0 and pos[1]+j>=0) and (pos[0]+i<=dim[0] and pos[1]+j<=dim[1]) and not(i==0 and j==0):
                adj.append([pos[0]+i,pos[1]+j])
    return adj