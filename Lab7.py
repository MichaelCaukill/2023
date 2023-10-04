companies = []
sales =[]
with open ("carSale.csv", "r") as file:
    lines = file.readlines()
    
for x in range(len(lines)):
    if x % 2 == 0:
        companies.append(lines[x])
    else:
        data = lines[x].strip().split(',')
        sales.append(list(map(int, data)))
        
for amount in sales[0]:
    

        
print(companies)
print(sales)
    
        
    
    
#\\\
