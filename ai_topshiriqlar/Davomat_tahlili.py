# Davomat tahlili
# Kurs: Dasturlash / IT
# Mavzu: O'zgaruvchilar ⭐ — yaratish va nomlash qoidalari (snake_case)
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
s = input().split()


print(s.count("1"))
print(len(max("".join(s).split("0"), key=len)))
print(int(s.count("1")) * 100 // n)