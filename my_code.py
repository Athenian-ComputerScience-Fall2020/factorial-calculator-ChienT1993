# Collaborators: https://beginnersbook.com/2018/02/python-program-to-find-factorial-of-number/
#  

def factorial_calc(x):
    fac= 1
    if x == 1:
        return x
    elif x == 0:
        return 1
    else:
        for i in range (1, x+1):
            fac= fac * i
        return fac



if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
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
