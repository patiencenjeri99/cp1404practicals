for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
for _ in range(number_of_stars):
    print("*", end='')
print()

n = int(input("Number of lines: "))
for i in range(1, n+1):
    print("*" * i)
