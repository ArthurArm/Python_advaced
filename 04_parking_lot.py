n = int(input())
data = set()

for _ in range(n):
    direction, plate = input().split(", ")
    if direction == "IN":
        data.add(plate)
    elif direction == "OUT":
        data.remove(plate)

if data:
    for car in data:
        print(car)
else:
    print("Parking Lot is Empty")

