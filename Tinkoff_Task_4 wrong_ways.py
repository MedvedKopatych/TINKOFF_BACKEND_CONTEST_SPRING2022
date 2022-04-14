"""def check_cut(stages, step):
    for i in range(0, len(stages)):
        j = i+1
        if sum(stages[i:j+1]) > step:
            print('appending i')
            converted.append(stages[i])

        elif sum(stages[i:j+1]) < step:
            j += 1
            if sum(stages[i:j+1]) == step:
                print('bingo')
                converted.append(sum(stages[i:j+1]))
                print(i)
                i = j+1
            else:
                j -= 1
                converted.append(sum(stages[i:j+1]))
                i = j
        else:
            converted.append(sum(stages[i:j+1]))
            i = j
"""

"""def check_cut(stages, step, capacity):
    for i in range(len(stages)-1):
        j = i + 1
        if stages[i] >= capacity:
            print('appending', i)
            converted.append(stages[i])
            i += 1
        elif stages[i] < capacity > sum(stages[i:j+1]):
            j += 1
            if sum(stages[i:j+1]) == capacity:
                converted.append(sum(stages[i:j + 1]))

            else:
                j -= 1
                converted.append(sum(stages[i:j + 1]))

        elif stages[i] < capacity < sum(stages[i:j + 1]):
            converted.append(stages[i])

            i += 1

    print(converted)"""

"""def check_cut(stages, step):
    print(stages)
    i = 0
    while i < len(stages):
        print(i)
        j = i+1
        if sum(stages[i:j+1]) > step:
            print(stages[i])
            i = j
            print(i, j)
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
    print('END')"""

stages = [3, 1, 1, 1, 1, 1, 1, 3]
groups = []

"""def check_out_2(stages, step, capacity):
    for i in range(len(stages)):
        if stages[i] <= capacity < sum(stages[i:i+2]):
            print('case 1')
            converted.append(stages[i])
            print(converted)
            print(i)
        i += 1
        print(i)
        if stages[i] < capacity == sum(stages[i:i+2]):
            print('case 2')
            converted.append(sum(stages[i:i+2]))
        i += 3
        if capacity > sum(stages[i:i+2]):
            j=i+1
            j += 1
            if sum(stages[i:j + 1]) == capacity:
                print('case 3-1')
                print(i, j)
                converted.append(sum(stages[i:j + 1]))
                print(converted)

            else:
                j -= 1
                print('case 3-2')
                converted.append(sum(stages[i:j + 1]))
                print(converted)

        i += j


    print(converted)"""

"""def check_cut(stages, step):
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
    else:
        print(i, j)"""


def check_out_2(stages, step, capacity):
    for i in range(len(stages)):

        if sum(stages[i:i + step]) <= capacity:
            converted.append(sum(stages[i:i + step]))
            """del stages[i:i+step]"""
            print("case2-1", stages[i:i + step], step)
            print(converted)
            i += step
            print(i)
            print(stages[i:])
        if sum(stages[i:i + step]) > capacity:
            j = step
            while sum(stages[i:i + j]) > capacity:
                j -= 1
                print("case2-2", stages[i:i + j])
                print(converted)
            converted.append(sum(stages[i:i + j]))
            i += j
            print("case2-3", stages[i:])
            print(converted)
            """del stages[i:i + step]"""
            print(i)
            print(stages[i:])

    """if len(stages[i:]) <= step:
        print("case 3", len(stages[i:]))
        if 
            print("case3-1")
            converted.append(stages[i])
            print("case3-1", stages)
            print(converted)
            i += 1
        else:
            print("case3-2", stages[i:])
            converted.append(sum(stages[i:]))
            print("case3-2", stages)"""

    print(converted)


check_out_2(stages, step, capacity)


def grouped(stages, step, capacity):
    pass