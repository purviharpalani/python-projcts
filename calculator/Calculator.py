logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


#Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def subtract(n1, n2):
    return n1 - n2

#Multiplication
def multiply(n1, n2):
    return n1 * n2

#Division
def divide(n1,n2):
    return n1 / n2

#Dictionary
operations ={
    '+' : add ,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

def calculator():
    num1 = float(input("What's the first number :"))
    for symbol in operations:
        print(symbol)
# operation_symbol = input("Pick an operation: ")
# num2 = int(input("What's the second number :"))
# calc_function = operations[operation_symbol]
# first_answer = calc_function(num1 , num2)
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    choice ='y'
    while choice=='y':
       operation_symbol = input("Pick an operation: ")
       num2 = float(input("What's the next number :"))
       calc_function = operations[operation_symbol]
       first_answer = calc_function(num1, num2)
       print(f"{num1} {operation_symbol} {num2} = {first_answer}")
       choice = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to start a new calculation:")
       if choice=='y':
           num1=first_answer
       if choice=='n':
           calculator()

calculator()