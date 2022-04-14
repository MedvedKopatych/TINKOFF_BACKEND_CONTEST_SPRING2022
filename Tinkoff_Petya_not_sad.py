from math import ceil

n = input()
A = list(map(int, input().split()))
number = 0
for a in sorted(A, reverse=True):
    number = ceil((number + a) ** .5)
print(number)
