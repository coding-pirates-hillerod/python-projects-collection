numbers = []

for i in range(3):
    num = int(input("Indtast et nummer: "))
    numbers.append(num)

biggest_number = max(numbers)

print(f"Det største nummer er: {biggest_number}")
