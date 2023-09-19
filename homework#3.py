# Task 1
try:
    day = int(input("Enter number of the day: "))
    if day in range(1, 8):
        match day: 
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
    else:
        raise Exception("Please enter valid number!")
except ValueError as e:
    print("Enter numbers only")
except Exception as e:
    print(f"Error: {e}")

# # Task 2
try:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    if n1 == n2:
        print("Numbers are equal")
    elif n1 > n2:
        print(n1, n2, end=" ")
    elif n1 < n2:
        print(n2, n1, end=" ")
except ValueError as e:
    print("Numbers only!")
except Exception as e:
    print(f"Error: {e}")

# Task 3
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    func = str(input("Enter function you want to use: \"+\", \"-\", \"*\" or \"/\": "))
    if func == "+":
        print(num1 + num2)
    elif func == "-":
        print(num1 - num2)
    elif func == "*":
        print(num1 * num2)
    elif func == "/":
        print(num1 / num2)
    else:
        raise Exception("Please enter a valid function!")
except ValueError as e:
    print("Numbers only")
except Exception as e:
    print(f"Error: {e}")
