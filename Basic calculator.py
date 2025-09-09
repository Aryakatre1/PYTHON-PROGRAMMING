def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid operator"

# User input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

print("Result:", calculator(a, b, op))

'''This is a simple calculator program in Python.

I wrote a function called calculator that accepts two numbers and an operator. Inside the function, I used conditional statements (if, elif, else) to check which operator the user selected.

If the operator is +, it performs addition.

If it’s -, it performs subtraction.

If it’s *, it performs multiplication.

If it’s /, it performs division, but I also added an error check so that if the second number is zero, it returns a friendly error message instead of crashing the program.
If the operator is not one of these four, it returns ‘Invalid operator’.

After defining the function, I take input from the user for both numbers and the operator. I convert the numbers into floats so the program supports decimals as well. Finally, I call the calculator function with those inputs and print the result.

This structure shows clean separation between logic (inside the function) and user interaction (taking inputs), which makes the program reusable and easy to maintain.”**

👉 Pro tip: If they ask how you can improve it, you can mention:

Adding more operators (%, **, etc.).

Using a dictionary mapping operators to functions instead of multiple if-else.

Handling invalid inputs with try-except.'''
