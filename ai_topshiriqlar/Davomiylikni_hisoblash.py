# Davomiylikni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

h1, m1, h2, m2 = [int(input()) for _ in range(4)]
d = (h2 * 60 + m2) - (h1 * 60 + m1)
print(d // 60, d % 60, sep="\n")