# Davomat tahlili
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
d = input().split()
c = d.count('1')
print(c, max(map(len, "".join(d).split('0'))), c * 100 // n, sep='\n')