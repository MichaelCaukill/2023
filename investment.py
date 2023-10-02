investment = int(input("enter initial investment "))
target = int(input("enter target investment "))
interest = float(input("enter interest rate "))
year = 0
while investment < target:
    year = year + 1
    investment = investment * interest
    print(investment)
    print(year, "Years")
