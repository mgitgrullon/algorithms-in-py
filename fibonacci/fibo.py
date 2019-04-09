# Memoization

# Option 1

# fibonacci_cache = {}

# def fibonacci(n):
#   # If we have cached the value, then return it
#   if n in fibonacci_cache:
#     return fibonacci_cache[n]

#   if n==1:
#     value = 1
#   elif n == 2:
#     value = 1 
#   elif n > 2:
#     value = fibonacci(n-1) + fibonacci(n-2)

#   # Cache the value and return it
#   fibonacci_cache[n] = value
#   return value


# for n in range(1, 101):
#   print(n, ":", fibonacci(n))


# Option 2

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
  # check that the input is a positive integer
  if type(n) != int:
    raise TypeError("n must be an Integer")
  if n < 1:
    raise ValueError("n must be positive Integer")

  if n == 1 or n == 2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)

# for n in range (10, 500):
#   print(n, ":", fibonacci(n))