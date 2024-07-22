def FirstFactorial(num):
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial


# keep this function call here 
print(FirstFactorial(input()))
