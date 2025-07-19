'''Write a Python function using match-case to perform basic arithmetic operations.
What will the function return when dividing 4 by 2 using the given operation?'''
def calculate(num1,num2,option):
    match option:
        case "+":
            res = num1 + num2
            return res
        case "-":
            res = num1 - num2
            return res
        case "*":
            res = num1 * num2
            return res
        case "/":
            res = num1 / num2
            return res
        case "":    # If no valid option is provided, return error message
            return "Invalid Option !"
       
print(calculate(4,2,"/"))

'''The given function calculate() takes two numbers and an operation symbol, 
then uses Python's match-case to select the correct arithmetic operation: addition, subtraction, multiplication, or division. 
If the operator doesn't match any case, it returns "Invalid Option !". 
When called with 4, 2, "/", it performs division and returns 2.0.'''