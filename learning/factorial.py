# write a function to calculate factorial

#recursive
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#iterative
def factorial_WithLoop(n):
    res = 1
    while n >= 1:
        res = n * res
        n  = n-1

    return res 
print(factorial_WithLoop(3))