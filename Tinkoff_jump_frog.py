"""mountain = int(input())
max_jump = map(int, input().split())
way_down = map(int, input().split())

ups = []
ups.extend(max_jump)
dwns = []
dwns.extend(way_down)

print(ups)
print(dwns)
dist = mountain
result = 0
def jump(dist, result):
    up = ups[dist-1]
    result += 1
    print(up)
    dist = dist - up
    print(dist)
    down = dwns[dist-1]
    print(down)
    dist = dist + down
    print(dist)
    if dist <= ups[dist-1]:
        result += 1
        print("Прыжков:", result)
    else:
        try:
            jump(dist,result)
        except RecursionError:
            print(-1, "Прыжков:", result)


jump(dist, result)
"""
distance = int(input())
jumps = [0] + list(map(int, input().split()))

slips = [0] + list(map(int, input().split()))

massive = [10 ** 9] * len(jumps)

for i in range(distance, 0, -1):
    massive[i] = max(0, i + slips[i] - jumps[i + slips[i]])

first = [10 ** 9 for i in range(len(jumps) + 2)]
second = [10 ** 9 for i in range(len(jumps) + 1)]
for i in range(distance, 0, -1):
    if min(i, massive[i]) < first[i + 1]:
        first[i] = min(i, massive[i])
        second[i] = i
    else:
        first[i] = first[i + 1]
        second[i] = second[i + 1]
height = distance
result = 0
i = 1
while i <= (distance and height):
    result += 1
    if first[height] >= height:
        break
    height = first[height]
if height != 0:
    print(-1)
else:
    print(result)
