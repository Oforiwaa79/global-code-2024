name = input("What is your name? ")
age = input("What is your age? ")

# check if age is an integer
if age.isdigit():
    age = int(age)
    y = "years" if int(age) > 1 else "year"

    if age < 0:
        print("Invalid age")
    # else:
    elif 0 > age <= 10:
        print(f"\nAt age {age}? You're a child dude")
    elif  10 > age <= 18:
        print(f"\nYoo {name} you're a teen. You're {age}{ y}.")
    else:
        print(f"\nWrite clean code dude, you're {age} {y}. Bela Chao {name.upper()}")
else:
    print("\nenter a number for age")

