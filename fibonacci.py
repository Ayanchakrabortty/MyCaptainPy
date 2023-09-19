
def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series
n = int(input("number of terms "))
fib_series = generate_fibonacci(n)
print("Fibonacci series:")
for num in fib_series:
    print(num, end=", ")
