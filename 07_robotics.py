from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(";"):                     # sorting the robots
    name, time_needed = r.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), __format="%H:%M:%S")     # time sorting
products = deque()

while True:                                                     # adding products in queue
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(days=0,  seconds=1)                    # 0 - days, 1 - seconds
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

            if value[1] == 0:
                free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
