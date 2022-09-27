from calculator_art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Store functions in a dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  not_finished = True
  
  while not_finished:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    cal_function = operations[operation_symbol]
    answer = cal_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if should_continue == "y":
      num1 = answer
    elif should_continue == "n":
      not_finished = False
      calculator()

calculator()