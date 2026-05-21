# Assignment 1 (types_and_vars.py)

# Bio
name = "Ugo" 
age = 10 
height = 1.82

print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")

# Future age
future_age = age + 5
print(f"In 5 years, I will be {future_age} years old.")

# Area of a rectangle
width = 5.5
rect_height = 2
area = width * rect_height
print(f"The area of a {width} x {rect_height} rectangle is {area}.")

# Demonstration
average = future_age - age / 2
print(f"My average age is {average}.")

print("Testing! " * 3)     # string repetition


# Assignment 2 (simple_calculator.py)

# Question
input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")

if input1.replace('.', '', 1).isdigit() and input2.replace('.', '', 1).isdigit():
    num1 = float(input1)
    num2 = float(input2)
else:
    print("Error: You must enter valid numbers.")
    exit()

operation = input("Choose an operation (+, -, *, /): ")

# Answer
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num1 / num2
else:
    print("Error: Unsupported operation.")
    exit()

# Calculator
print(f"{num1} {operation} {num2} = {result}")


# Assignment 3 (string_fun.py)

word = input("Enter a word: ")

print(f"The length of the word is: {len(word)}")

print(f"In uppercase: {word.upper()}")

print(word * 3)


