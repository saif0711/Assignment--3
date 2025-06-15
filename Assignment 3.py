#Task-1
n=int(input("Enter a number:"))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(n)
print(f'Factorial of {n} is:',result)

#Task-2
n=int(input("Enter a number:"))
import math
square_root = math.sqrt(n)
print('Square root:',square_root)

log = math.log(n)
print('Logarithm:',log)

sine_value = math.sin(n)
print(f'Sine:',sine_value)

