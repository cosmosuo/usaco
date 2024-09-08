# calculate the nTh number in fibonnacci sequence
#def fibonacci(n):
 #   if n == 1:
 #       return 1
  #  else:
  #      return n * fibonacci(n-2) + (n-1))

#f(n) = f(n-2) + f(n-1)

#0, 1, 1, 2, 3, 5, 8, 13, 21,...

#f(n) = f(n - 2) + f(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(100))