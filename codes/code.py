import numpy as np
import pandas as pd
read = pd.read_excel("input.xlsx","Sheet1")
data = np.array(read)
values = list(data[0])
o = values.count('O')
a = values.count('A')
b = values.count('B')
ab = values.count('AB')
blood_groups = ['O','A','B','AB']
frequencies = [o,a,b,ab]
maximum = max(o,a,b,ab)
minimum =  min(o,a,b,ab)
dictionary = {o:'O',a:'A',b:'B',ab:'AB'}
print(f'The Most common Blood group : {dictionary[maximum]}')
print(f'The rarest Blood group      : {dictionary[minimum]}')
write = pd.DataFrame({"Blood Groups":blood_groups,"Frequency":frequencies})
write.to_excel("output.xlsx",index=False)
