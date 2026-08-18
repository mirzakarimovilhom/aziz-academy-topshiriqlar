# Bank: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

import sys 


data = sys.stdin.read().split()
if data:
    n = int(data[0])
    total_rev, max_rev, best_name, total_qty = 0, -1, "", 0
    
    
    idx = 1
    for _ in range(n):
        nom, narx, soni = data[idx], int(data[idx + 1]), int(data[idx + 2])
        idx += 3 
        
        
        tushum = narx * soni
        total_rev += tushum
        total_qty += soni 
        
        
        if tushum > max_rev:
            max_rev = tushum
            best_name = nom
            
            
    print(total_rev)
    print(best_name)
    print(total_qty)