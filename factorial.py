import threading
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial(number):
    result = factorial(number)
    print(f"Factorial of {number} is {result}")

n = int(input("Enter an integer to calculate its factorial: "))
factorial_thread = threading.Thread(target=calculate_factorial, args=(n,))
factorial_thread.start()
factorial_thread.join()
