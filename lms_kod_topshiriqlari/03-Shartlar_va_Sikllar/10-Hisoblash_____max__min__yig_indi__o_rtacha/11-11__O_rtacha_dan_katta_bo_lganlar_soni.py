import sys


data = list(map(int, sys.stdin.read().split()))
if data:
    n, nums = data[0], data[1:]
    avg = sum(nums) / n 
    print(sum(1 for x in nums if x > avg))