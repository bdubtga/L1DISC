numbers = []
while True:
  number = input("Enter a number: ")
  if number == "quit":
    break
  else:
    numbers.append(int(number))
for number in numbers:
  if number % 2 == 1:  # Check if the number is odd
    print(number)