# Taksi park: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n, s, t = int(input()), 0, 0 
for _ in range(n):
    b = int(input())
    if s + b <= 100000:
        s += b 
        t += 1 
    else:
        break
print(t, s, n - t, sep="\n")