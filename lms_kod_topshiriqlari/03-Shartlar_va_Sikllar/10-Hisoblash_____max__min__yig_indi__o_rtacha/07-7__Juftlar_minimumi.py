n = int(input())
a = list(map(int, input().split()))
e = [x for x in a if x % 2 == 0]


print(min(e) if e else 'No')