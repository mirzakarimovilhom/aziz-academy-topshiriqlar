l = []
while (n := int(input())) != 0:
    l.append(n)
print(sum(l) / len(l) if l else 0)