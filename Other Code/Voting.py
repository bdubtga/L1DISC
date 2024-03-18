"""Script detrimine NZ voting elegibility based on age and residency."""

name = str(input("What is your name?\n"))
# ask and validate age
while True:
    age = input("How old are you?\n")
    try:
        try:
            age = int(age)
        except:
            raise ValueError(f"Please enter a number.")
        if age < 0:
            raise ValueError(f"Please enter a number greater than 0.")
        if age > 120:
            raise ValueError(f"Please enter a number less than 120.")
        break
    except ValueError as e:
        print(f"{age} is not a valid age. {e}")
# ask and validate residency
while True:
    try:
        is_resident_input = str(
            input("Are you a resident of New Zealand? (yes/no)\n")
        ).lower()
        if is_resident_input not in ["yes", "no", "y", "n"]:
            raise ValueError("Please enter 'yes' or 'no'.")
        else:
            break
    except ValueError as e:
        print(f"Invalid input: {e}")
# determine eligibility
is_resident = is_resident_input == "yes" or "y"
if age >= 17 and is_resident:
    print(f"{name}, you are eligible to vote in New Zealand.")
else:
    print(f"{name}, you are not eligible to vote in New Zealand.")
