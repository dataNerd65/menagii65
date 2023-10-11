x = float(input("Enter first Number:"))
y = float(input("Enter second Number:"))


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
     return("Math Error!")
    else:
     return x / y
 
    
while True:
    print("Please select operation to use.:")
    try:
     print("1, Add.")
     print("2, Subtract.")
     print("3, Multiply.")
     print("4, Divide.")
     print("5, Exit.")


     choice = input("Enter 1, 2, 3, 4, 5 for operation you want.")
    except:
       print("Invalid Choice.")

    if choice == "1":
       print(x + y)
    elif choice == "2":
       print(x - y)
    elif choice == "3":
       print(x * y)
    elif choice == "4":
       print(x / y)
    elif choice  == "5":
       print("Calculator closing...!")
       break
    

    
    
