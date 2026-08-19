# Vaqtni birliklarga ajratish
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

T = int(input())


kun = T // 86400 
T %= 86400 


soat = T // 3600 
T %= 3600 


daqiqa = T // 60 
sekund = T % 60 


print(kun)
print(soat)
print(daqiqa)
print(sekund)