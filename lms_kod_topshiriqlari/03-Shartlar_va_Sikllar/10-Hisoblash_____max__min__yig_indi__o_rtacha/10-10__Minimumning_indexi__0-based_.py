n = int(input())
numbers = list(map(int, input().split()))


min_index = numbers.index(min(numbers))


print(min_index)