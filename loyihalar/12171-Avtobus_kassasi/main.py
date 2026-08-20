# Avtobus kassasi
# Buyruqlar: sozla <soni>, sot <raqam> <ism>, qaytar <raqam>, xarita, hisobot, exit
joylar = None   # sozla'dan keyin: [None, None, ...] (None = bo'sh)
while True:
    cmd = input().strip()
    if cmd == 'exit':
        break
    # TODO: buyruqlarni shu yerda qayta ishlang
