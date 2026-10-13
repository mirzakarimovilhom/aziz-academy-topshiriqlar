# Valyuta konvertori
# Buyruqlar: kurs <valyuta> <qiymat>, kurslar, convert <summa> <valyuta>, tarix, hisobot, exit
kurslar = {}   # masalan: {'USD': 12500}
tarix = []     # har element: (summa, valyuta, natija)
while True:
    cmd = input().strip()
    if cmd == 'exit':
        break
    # TODO: buyruqlarni shu yerda qayta ishlang
