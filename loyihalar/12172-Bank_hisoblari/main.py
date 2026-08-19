from hisob import yangi_hisob


hisoblar = {}
keyingi_raqam = 1001


while True:
    cmd = input().strip()
    if not cmd:
        continue
        
        
    parts = cmd.split(maxsplit=1)
    amal = parts[0]
    
    
    if amal == "och" and len(parts) > 1:
        ism = parts[1]
        hisoblar[keyingi_raqam] = yangi_hisob(ism)
        print(f"Hisob ochiladi: {keyingi_raqam} _ {ism}")
        keyingi_raqam += 1