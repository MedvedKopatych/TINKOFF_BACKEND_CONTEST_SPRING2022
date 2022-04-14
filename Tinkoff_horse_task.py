n, m = map(int, input().split())
massive = []
for i in range(n):
    massive.append(list([-1 for j in range(m)]))
massive[n-1][0] = 1


def horse(i, j):
    if 0 <= i < n and m > j >= 0:
        if massive[i][j] == -1:
            massive[i][j] = horse(i+2, j-1)+horse(i+1, j-2)
    else:
        return 0
    return massive[i][j]


print(horse(0, m-1))
