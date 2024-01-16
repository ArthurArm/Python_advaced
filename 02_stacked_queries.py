numbers = []

for _ in range(int(input())):
    num_data = input().split()
    command = num_data[0]
    if command == "1":
        numbers.append(num_data[1])
    elif command == "2":
        if numbers:
            numbers.pop()
    elif command == "3":
        if numbers:
            print(max(numbers))
    elif command == "4":
        if numbers:
            print(min(numbers))

numbers.reverse()

print(*numbers, sep=", ")

                                # separator (sep=)



