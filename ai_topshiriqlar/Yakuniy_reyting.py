# Yakuniy reyting
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

import sys


d = sys.stdin.read().split()
n = int(d[0])
p = [(d[i], int(d[i + 1])) for i in range(1, 2 * n, 2)]


p.sort(key=lambda x: (-x[1], x[0]))
avg = sum(x[1] for x in p) // n 


print(p[0][0])
print(avg)
print(sum(1 for x in p if x[1] > avg))