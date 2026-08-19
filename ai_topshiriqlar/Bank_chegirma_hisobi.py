# Bank: chegirma hisobi
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

narx1 = int(input())
narx2 = int(input())


jami = (narx1 * 0.7) + (narx2 * 0.7)


if jami < 100000:
    jami += 10000
    
    
print(int(round(jami)))