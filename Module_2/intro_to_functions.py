# Defining a function:
def double_it(num):
    result = num *2
    print(result)
    return result

double_it(7)
double_it(45)

# Defining a function with multiple parameter:
def sum(n1,n2):
    result = n1+n2
    return result

total = sum(4,9)
print("Total Sum = ",total)

#calling function within function:
finalValue = double_it(total)
print("Final output : ",finalValue)