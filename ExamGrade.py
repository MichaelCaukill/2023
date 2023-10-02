level = int(input("Please enter your level "))
grade = int(input("Please enter your grade "))
if level == 1:
    if grade < 50:
        Print("Fail")
    elif grade >= 50 and grade <= 60:
        print("Pass")
    elif grade >=61 and grade <= 70:
        print("Merit")
    elif grade >=71 and grade <= 100:
        print("Distinction")
    else:
        print("Please enter a number between 1 and 100")
elif level == 2:
    if grade < 40:
        Print("Fail")
    elif grade >= 40 and grade <= 50:
        print("Pass")
    elif grade >=51 and grade <= 65:
        print("Merit")
    elif grade >=66 and grade <= 100:
        print("Distinction")
    else:
        print("Please enter a number between 1 and 100")
else:
    print("Please enter a valid number")
