from collections import deque

name = input()

customer = deque()

while name != "End":
    if name == "Paid":
        while customer:
            print(customer.popleft())
    else:
        customer.append(name)
    name = input()

print(f"{len(customer)} people remaining.")
