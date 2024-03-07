#Program to make as simple calculator

#This function adds two numbers
def add(x, y):
    return x + y

#This function substracts two numbers
def substract(x, y):
    return x - y

#this function multiplies two numbers
def multiply(x, y):
    return x * y

#This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation")
print("1.Add")
print("2.Substract")
print("3.multiply")
print("4.Divide")

while True:
    #take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    #check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", substract(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))
        
        elif choice == '4':
            print(a,"/", b, "=", divide(a, b))

        #check if the user want to another calculation
        #break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Invalid Input")
