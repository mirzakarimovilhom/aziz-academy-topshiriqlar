# Yakuniy reyting
# Kurs: Dasturlash / IT
# Mavzu: O'zgaruvchilar ⭐ — yaratish va nomlash qoidalari (snake_case)
# Ball: 100
# Aziz Academy — AI Topshiriq

d = [input().split() for _ in range(int(input()))]
s = [int(b) for _, b in d]
print(
    min(d, key=lambda x: (int(x[1]), x[0]))[0],
    sum(s) // len(d),
    sum(b > sum(s) // len(d) for b in s),
    sep="\n",
)