# Davomiylikni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())


start_minutes = h1 * 60 + m1 
end_minutes = h2 * 60 + m2 


diff_minutes = end_minutes - start_minutes


hours = diff_minutes // 60
minutes = diff_minutes % 60 


print(hours)
print(minutes)