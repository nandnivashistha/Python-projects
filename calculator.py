from replit import clear
from art import logo
def add(n1, n2):
  '''adds no.1 and no.2'''
  return n1+n2
def subtract(n1, n2):  
  '''subtract no.2 from no.1'''
  return n1-n2
def multiply(n1, n2):
  '''multiply no.1, no.2 times'''
  return n1*n2
def devide(n1, n2):
  '''devide no.1 from no.2'''
  return n1/n2
def power(n1, n2):
  '''raises no.1 to the power no.2'''
  return n1**n2

operations={
  '+':add ,
  '-':subtract,
  '*':multiply,
  '/':devide,
  '**':power,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
