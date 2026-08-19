a, b, op = input().split()
a, b = int(a), int(b)
print(a + b if op == "+" else a - b if op == "-" else "Invalid")