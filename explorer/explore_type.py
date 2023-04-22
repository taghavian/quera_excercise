import os


def explore(ttype, address):
    ans=dict()
    for i in os.walk(address):
        s=0
        for j in i[2]:
            if os.path.basename(j).lower().split(".")[1]==ttype:
                s+=1
        if s>0:
            ans[i[0]]=s
    return ans

sol=explore('txt','.')
b=1
    
