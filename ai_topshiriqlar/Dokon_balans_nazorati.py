# Do'kon: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

b = m = 500000
w = 0 
for _ in range(int(input())):
    o = input()
    b += int(o)
    w += "-" in o
    m = min(m, b)
print(b, m, w, sep="\n")