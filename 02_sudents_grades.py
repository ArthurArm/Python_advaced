n = int(input())

d = {}
for _ in range(n):
     name, grades = input().split()
     grade = float(grades)

     if name not in d:
          d[name] = []
     d[name].append(grade)

for name, grades in d.items():
     avr = sum(grades) / len(grades)
     form = f'{" ".join([f"{g:.2f}" for g in grades])}'
     print(f"{name} -> {form} (avg: {avr:.2f})")