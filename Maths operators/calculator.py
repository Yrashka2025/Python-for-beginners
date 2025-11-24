print("For exit write 'q'")
while True:
    s = input("Sign (+, -, *, /): ")
    if s == "q":
        break
    if s in ('+', '-', '*', '/'):
        try:
            x = float(input("x = "))
            y = float(input("y = "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        if s == '+':
            print(f"{x} + {y} = {x + y}")
        elif s == '-':
            print(f"{x} - {y} = {x - y}")
        elif s == '*':
            print(f"{x} * {y} = {x * y}")
        elif s == '/':
            if y == 0:
                print("Division by zero is not allowed.")
            else:
                print(f"{x} / {y} = {x / y}")
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
