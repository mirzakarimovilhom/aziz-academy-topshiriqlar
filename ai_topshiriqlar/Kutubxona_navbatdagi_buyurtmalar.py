# Kutubxona: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Arifmetik operatorlar — + - * / // % ** va prioritet
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
cnt, s = 0, 0 


for _ in range(n):
    val = int(input())
    if s + val <= 50000:
        s += val
        cnt += 1
    else:
        break
        
print(cnt)
print(s)
print(n - cnt)