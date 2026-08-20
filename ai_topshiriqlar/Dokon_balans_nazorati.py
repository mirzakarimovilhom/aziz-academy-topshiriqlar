# Do'kon: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: O'zgaruvchilar ⭐ — yaratish va nomlash qoidalari (snake_case)
# Ball: 100
# Aziz Academy — AI Topshiriq

b = m = 200000 
w = 0 
for _ in range(int(input())):
    o = input()
    b += int(o)
    w += o[0] == '-'
    m = min(m, b)
print(b, m, w, sep='\n')