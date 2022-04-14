# Task1
"""total_mass, block_mass, coin_mass = map(int, input().split())


def production(total_mass, block_mass, coin_mass,coins = 0):
    while True:
        if total_mass >= block_mass:
            total_mass -= block_mass
            coins += block_mass // coin_mass
            total_mass += block_mass % coin_mass
        else:
            break
    print(coins)


production(total_mass, block_mass, coin_mass, coins=0)"""

# Task 4
"""stages, step, capacity = map(int, input().split())"""

""""""
stages = [3, 1, 1, 1, 2, 2, 3, 1, 1, 2, 1]
step = 2
capacity = 3
converted = []
groups = []


def check_cut(stages, capacity, step):
    i = 0
    while i < len(stages):
        j = i+1
        if sum(stages[i:j+1]) > capacity or len(stages[i:j+1]) > step:
            converted.append(stages[i])
            i = j
        elif sum(stages[i:j+1]) < capacity and len(stages[i:j+1]) <= step:
            while sum(stages[i:j+1]) < capacity and len(stages[i:j+1]) <= step:
                j += 1
            if sum(stages[i:j+1]) == capacity and len(stages[i:j+1]) <= step:
                converted.append(sum(stages[i:j+1]))
                groups.append([i, j]) if j < len(stages) else False
            else:
                j -= 1
                converted.append(sum(stages[i:j + 1]))
                groups.append([i, j]) if j < len(stages) else False
            i = j+1

        else:
            converted.append(sum(stages[i:j + 1]))
            groups.append([i, j]) if j < len(stages) else False
            i = j+1

    print(converted)
    print(groups)
    print('can use', (len(groups)), 'less batteries')


check_cut(stages, capacity, step)


# Task
