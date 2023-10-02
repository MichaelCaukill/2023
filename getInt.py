minimum = 1
maximum = 100
attempts = 1
while attempts < 4:
    num1 = int(input("Enter number"))
    attempts = attempts + 1
    if num1 <= maximum and num1 >= minimum:
        print(num1)
    else:
        if attempts > 3:
            print("None")
    
