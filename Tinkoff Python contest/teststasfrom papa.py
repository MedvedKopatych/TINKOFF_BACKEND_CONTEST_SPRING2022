stages = [3, 1, 1, 1, 1, 1, 1, 3]
step = 4


def check_cut(stages, step):
    i = 0
    while i < len(stages):
        j = i+1
        if sum(stages[i:j+1]) > step:
            print(stages[i])
            i = j
        elif sum(stages[i:j+1]) < step:
            while sum(stages[i:j+1]) < step:
                j += 1
            if sum(stages[i:j+1]) == step:
                print(stages[i:j+1])
            else:
                j -= 1
                print(stages[i:j+1])
            i = j+1

        else:
            print(stages[i:j + 1])
            i = j+1

    print(i, j)


check_cut(stages, step)

