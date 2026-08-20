# Do'kon: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

data = [*map(int, open(0).read().split())]
n = data[0]
s = c = 0
for x in data[1:]:
    if s + x <= 100000:
        s += x 
        c += 1
    else:
        break
print(c, s, n - c, sep="\n")