# Do'kon: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
s, c = 0, 0 
for i in range(n):
    p = int(input())
    if s + p <= 50000:
        s += p 
        c += 1 
    else:
        break
print(c, s, n - c, sep="\n")