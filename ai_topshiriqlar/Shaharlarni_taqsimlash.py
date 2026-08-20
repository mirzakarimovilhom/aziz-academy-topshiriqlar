# Shaharlarni taqsimlash
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
k = int(input())


share = n // k
rem = n % k
need = 0 if rem == 0 else k - rem 


print(share, rem, need, sep='\n')