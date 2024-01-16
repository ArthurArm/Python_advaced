clother = [int(x) for x in input().split()]

rack_space = int(input())

racks_count = 1
cur_rack_sp = rack_space

while clother:

    cloth = clother.pop()

    if cur_rack_sp >= cloth:
        cur_rack_sp -= cloth
    else:
        racks_count += 1
        cur_rack_sp = rack_space - cloth

print(racks_count)

