
print("1. Add + ")
print("2. Subtract - ")
print("3. Multiply * ")
print("4. Divide / ")
print("5. Square s ")
option = int(input("Please select which option "))

if option == 1:
    number1 = int(input("Enter the first number "))
    number2 = int(input("Enter the second number "))
    addition = (number1+number2)
    print(addition)
elif option == 2:
    number1 = int(input("Enter the first number "))
    number2 = int(input("Enter the second number "))
    subtraction = (number1-number2)
    print(subtraction)
elif option == 3:
    number1 = int(input("Enter the first number "))
    number2 = int(input("Enter the second number "))
    multiply = (number1*number2)
    print(multiply)
elif option == 4:
    number1 = int(input("Enter the first number "))
    number2 = int(input("Enter the second number "))
    division = (number1/number2)
    print(division)
elif option == 5:
    number1 = int(input("Enter the number you wish to square "))
    square = (number1**2)
    print(square)
else:
    print("Enter a valid number")
