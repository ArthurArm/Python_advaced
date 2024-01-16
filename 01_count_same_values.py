numbers = tuple([float(x) for x in input().split()])
coount = {}
for num in numbers:
    if num not in coount:
        coount[num] = numbers.count(num)

for num, occ in coount.items():
    print(f"{num} - {occ} times")
