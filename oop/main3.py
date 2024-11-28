from class_static_methods_demo import Calculator

def main() :
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

   
    sum_multiple = Calculator.multiply(10, 5)
    print(f"The sum is: {sum_multiple}")
    
    
if __name__=="__main__" :
    main()
