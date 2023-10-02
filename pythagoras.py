print("""
        Pythagoras' Calculator
        -------------------------------------
        1. Find the length of A given B and C
        2. Find the length of B given A and C
        3. Find the length of C given A and B
        -------------------------------------
        """)
option = int(input("Please enter which option "))
if option == 1:
             b = int(input("Enter value of B "))
             c = int(input("Enter value of C "))
             a = (((c**2) - (b**2))**0.5)           
             print("The length of A is ", a)
elif option == 2:
             a = int(input("Enter value of A "))
             c = int(input("Enter value of C "))
             b = (((c**2) - (a**2))**0.5)           
             print(b)
elif option == 3:
             a = int(input("Enter value of A "))
             b = int(input("Enter value of B "))
             c = (((a**2) + (b**2))**0.5)           
             print(c)
else:
    print("Enter a valid option")
