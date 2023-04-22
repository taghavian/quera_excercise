import os


def explore(ttype, address):
    ans=dict()
    for i in os.walk(address):
        s=0
        for j in i[2]:
            if len(os.path.basename(j).lower().split("."+ttype.lower()))>1:
                s+=1
        if s>0:
            ans[i[0]]=s
    return ans

a=explore("jpg", "/test_media")
b=1
    
