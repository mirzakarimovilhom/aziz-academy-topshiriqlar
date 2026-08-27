# Aloqa do'koni: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: Stringlar — kirish: matn, qo'shtirnoqlar, len()
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
R, Q, M, B = 0, 0, -1, ""
for _ in range(n):
    name, price, qty = input().split()
    rev = int(price) * int(qty)
    R += rev 
    Q += int(qty)
    if rev > M:
        M, B = rev, name
print(f"{R}\n{B}\n{Q}")