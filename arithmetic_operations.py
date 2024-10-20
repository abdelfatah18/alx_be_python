def perform_operation(num1,num2,operation) :
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  operation = input("add, subtract, multiply, divide):")
 
  if operation == "add":
        result = num1 + num2
        print(f"{num1} + {num2} is {result}.")
  elif operation == "subtract":
         result = num1 - num2
         print(f"{num1} - {num2} is {result}.")
  elif operation == "multiply":
        result = num1 * num2
        print(f"{result}.")
  elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f" {result:.2f}.")  
perform_operation(num1,num2,operation)