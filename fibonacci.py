print("Welcome!!!  \nThis Fibonacci program:")

def fibonacci(n):
    a = 0
    b = 1
                
    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")
                                            
    # Check if n is equal to 0
    elif n == 0:
        return 0
                                                                  
    # Check if n is equal to 1
    elif n == 1:
        return b
    
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

m = int(input("Enter m (position in Fibonacci sequence): "))
print(fibonacci(m))

#The following line will be both chaged by branch 1 & branch 2 
print("End of program. bye bye!")
