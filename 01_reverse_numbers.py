from collections import deque

# solution 1.0
numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")


# solution 1.1

numbers = deque(input().split())

numbers.reverse()

#print(" ".join(numbers))
print(*numbers)                        # star (*) means unpack list or else
