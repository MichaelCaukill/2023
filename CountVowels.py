mystring = input("Please enter your word ")
vowels = 'aeiou'
count = 0
for letter in mystring:
    if letter.lower() in vowels:
        count += 1
print("The number of vowels is: ", count)
