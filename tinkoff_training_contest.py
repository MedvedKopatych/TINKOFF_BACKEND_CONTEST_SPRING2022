# Task 1
"""month_price, month_traffic, extra_price, planed_traffic = map(int, input().split())
if planed_traffic <= month_traffic:
    cost = month_price
else:
    cost = month_price + extra_price*(planed_traffic - month_traffic)
print(cost)"""

# Task 2

# Task 3
"""staff, deadline = map(int, input().split())
floors = list(map(int, input().split()))
deadline_floor = int(input()) - 1


def check_deadline(deadline, floors, deadline_floor):
    if floors[deadline_floor] - floors[0] > deadline:
        first = floors[deadline_floor]
        print(first)
    else:
        first = floors[0]
        print(first)
    return first


def run(floors, first=check_deadline(deadline, floors, deadline_floor)):
    if first != floors[0]:
        time_up_down = max(floors) - min(floors) \
            + max(floors) - first
        print(time_up_down)
        time_down_up = max(floors) - min(floors) \
            + first - min(floors)
        print(time_down_up)
        rational_time = min(time_down_up, time_up_down)
    else:
        rational_time = max(floors) - min(floors)
    return rational_time


check_deadline(deadline, floors, deadline_floor)
run(floors, first=check_deadline(deadline, floors, deadline_floor))"""



