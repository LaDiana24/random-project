#Phyton program to find the factors of a number

#This function computes the factor of the argument passed
def print_factors(x):
    print("the factors of" ,x,"are")
    for i in range(1, x +1):
        if x % 1 == 0:
            print(i)

num = input("Enter the number: ")
print_factors(num)