from collections import deque

stations = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

station_copy = stations.copy()
gas = 0
index = 0

while station_copy:
    petrol, distance = station_copy.popleft()

    gas += petrol

    if gas >= distance:
        gas -= distance
    else:
        stations.rotate(-1)
        station_copy = stations.copy()
        index += 1
        gas = 0

print(index)
