# O'yin klubi: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

d = [input().split() for _ in range(int(input()))]
s = [int(p) * int(c) for _, p, c in d]
print(
   sum(s),
   max(zip(s, d))[1][0],
   sum(int(c) for _, _, c in d),
    sep="\n",
)