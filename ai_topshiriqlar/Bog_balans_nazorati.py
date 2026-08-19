# Bog': balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

import sys 


data = sys.stdin.read().split()
bal = min_bal = 100000
exp = 0


for op in data[1:]:
    x = int(op[1:])
    bal += x if op[0] == "+" else -x
    if op[0] == "-":
        exp += 1
    min_bal = min(min_bal, bal)
    
    
print(f"{bal}\n{min_bal}\n{exp}")