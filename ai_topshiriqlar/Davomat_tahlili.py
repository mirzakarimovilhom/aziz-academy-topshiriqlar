# Davomat tahlili
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
days = list(map(int, input().split()))


total_present = sum(days)


max_streak = 0
current_streak = 0
for day in days:
    if day == 1:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0 
        
        
percentage = (total_present* 100) // n 


print(total_present)
print(max_streak)
print(percentage)