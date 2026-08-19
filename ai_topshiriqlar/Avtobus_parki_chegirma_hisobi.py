# Avtobus parki: chegirma hisobi
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

narx1 = int(input())
narx2 = int(input())


umumiy = (narx1 + narx2) * 0.85


if umumiy < 100000:
    umumiy += 10000
    
    
print(int(umumiy))