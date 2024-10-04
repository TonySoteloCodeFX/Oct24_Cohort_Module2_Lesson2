print("------")
print("Task #1")

numbers_asked = []

count = 0
while count < 3:
    number = int(input("Enter a number: "))
    numbers_asked.append(number)
    count += 1
print(f"The largest number is {max(numbers_asked)}")

print("------")
print("Task #2")
print(f"The smallest number is {min(numbers_asked)}")
print("------")