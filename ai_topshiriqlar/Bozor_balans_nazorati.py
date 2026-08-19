# Bozor: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

import sys 


data = sys.stdin.read().split()
N = int(data[0])


bal = 100000
min_bal = 100000
exp = 0


for i in range(1, N + 1):
    op = data[i]
    x = int(op[1:])
    if op[0] == "+":
        bal += x
    else:
        bal -= x
        exp += 1
    if bal < min_bal:
        min_bal = bal
        
        
print(bal)
print(min_bal)
print(exp)