def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def main():
  
  print("Welcome to the simple calculator!")

  
  number_1 = float(input("Enter the first number: "))
  number_2 = float(input("Enter the second number: "))

 
  print("What would you like to do?")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  
  choice = input("Enter your choice: ")

 
  if choice == "1":
    print("The sum is:", add(number_1, number_2))
  elif choice == "2":
    print("The difference is:", subtract(number_1, number_2))
  elif choice == "3":
    print("The product is:", multiply(number_1, number_2))
  elif choice == "4":
    print("The quotient is:", divide(number_1, number_2))
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()