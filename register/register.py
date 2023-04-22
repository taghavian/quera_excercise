from re import *

def check_registration_rules(**kwargs):
    a=kwargs.copy()
    for i in kwargs:
        if len(kwargs[i])<6 or len(i)<4 or i=='quera' or i=='codecup' or   match("^\d+$",kwargs[i]):
            a.pop(i)
    
    return list(a.keys())
        
# b=check_registration_rules(username='password', sadegh='He3@lsa')
check_registration_rules()