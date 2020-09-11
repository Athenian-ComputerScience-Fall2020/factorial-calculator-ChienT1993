# Collaborators: https://beginnersbook.com/2018/02/python-program-to-find-factorial-of-number/
#  

def factorial_calc(x):   #you may choose the name of the parameter

    return    # be sure to return the factorial


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    

    if x == 1:
        return x
    else:
        return x * factorial_calc(x-1)
        
x = int(input("Enter value to factorialize: "))

if x < 0:
    print("Factorial cannot be found for negative numbers")
elif x == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", x, "is: ", factorial_calc(x))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
