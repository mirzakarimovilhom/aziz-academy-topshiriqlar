# Do'kon: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Stringlar — kirish: matn, qo'shtirnoqlar, len()
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
c, s = 0, 0 
for _ in range(n):
    x = int(input())
    if s + x <= 100000:
        s += x 
        c += 1 
    else:
        break
print(f"{c}\n{s}\n{n - c}")