import numpy as np
a =0
b =0
o =0
ab =0
data = ['A','B','O','O','AB','O','A','O','B','A','O','B','A','O','O','A','AB','O','A','A','O','O','AB','B','A','O','B','A','B','O']
for i in data :
    if(i=='O'): o +=1
    if(i=='A'): a +=1
    if(i=='B'): b +=1
    if(i=='AB'): ab +=1 
print(f'Frequency of Blood Group O  : {o} ')
print(f'Frequency of Blood Group A  : {a} ')
print(f'Frequency of Blood Group B  : {b} ')
print(f'Frequency of Blood Group AB : {ab}')
table = {o:'O', a:'A', b:'B', ab:'AB'}
print(f'Most common Blood Group : {table[max(o,a,b,ab)]}')
print(f'Rarest Blod group : {table[min(o,a,b,ab)]} ')