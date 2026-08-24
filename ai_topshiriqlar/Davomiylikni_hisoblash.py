# Davomiylikni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: O'zgaruvchilar ⭐ — yaratish va nomlash qoidalari (snake_case)
# Ball: 100
# Aziz Academy — AI Topshiriq

h1, m1, h2, m2 = [int(input()) for _ in range(4)]
t = (h2 * 60 + m2) - (h1 * 60 + m1)
print(t // 60, t % 60, sep='\n')