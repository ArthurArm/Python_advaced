n = int(input())
reservations = set()

for _ in range(n):
    codes = input()
    reservations.add(codes)
guests = input()
while guests != "END":
    if guests in reservations:
        reservations.remove(guests)
    guests = input()
print(len(reservations))
for g in sorted(reservations):
    print(g)
