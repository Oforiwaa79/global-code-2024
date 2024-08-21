name = input("What is your name? ")
age = input("What is your age? ")
# print(type(age))

print("Hello " + name+  "! You are " + age + " old.")

# y = "years" if int(age) > 1 else "year"
y = "" 
if int(age) > 1: 
    y = "years"
else:
    y = "year"

print("Hello " + name + "! You are " + age + " " + y + " old.")