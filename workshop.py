def factorial(n):
    if n == 1:
       return 1

    return n*factorial(n-1)

print(factorial(4))

#fibonacci
a,b = 1,1
print(a)
print(b)
for _ in range(10):
  print(a+b)
  a,b = b,a+b

#fib func
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Here is the 10th Fibonacci number",fibonacci(10))



