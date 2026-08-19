numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
