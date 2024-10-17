number = int(input("Enter a number to see its multiplication table: "))
x= range(1, 11)

for i in range(1, 11):  
   product = number * i
   print(f"{number} * {i} = {product}")  
