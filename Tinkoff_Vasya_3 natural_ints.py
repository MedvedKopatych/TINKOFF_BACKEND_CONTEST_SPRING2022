summation, subtraction, number = map(int, input().split())

if (summation - subtraction) >= number and (summation - subtraction) % 2 == 0:
    print("Yes")
else:
    print("No")
