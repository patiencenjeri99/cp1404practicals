"""1. Write name to file"""
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read name from file and print greeting
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers and add them
with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    result = num1 + num2
    print(result)

# 4. Total all numbers in file
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
