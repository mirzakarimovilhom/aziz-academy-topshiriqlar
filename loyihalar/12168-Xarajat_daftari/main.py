# Xarajat daftari
# Buyruqlar: kirim <summa>, chiqim <summa>, balans, tarix, hisobot, exit
balans = 0
amallar = []   # har element: '+10000' yoki '-3000' ko'rinishida
while True:
    cmd = input().strip()
    if cmd == 'exit':
        break
    # TODO: buyruqlarni shu yerda qayta ishlang
