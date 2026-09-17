n = int(input())
print(sum(1 for x in map(int, input().split()) if x % 3 == 0))