n = int(input())
print(sum(x for x in map(int, input().split()) if x > 10))