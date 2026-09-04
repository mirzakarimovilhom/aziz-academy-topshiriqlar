# Mashg'ulotlarni taqsimlash
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

N = int(input())
K = int(input())


ulush = N // K
qoldiq = N % K 


if qoldiq == 0:
    yetishmayotgan = 0 
else:
    yetishmayotgan = K - qoldiq 
    
    
print(ulush)
print(qoldiq)
print(yetishmayotgan)