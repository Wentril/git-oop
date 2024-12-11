print("Hello world")


def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print("Hi")
# function to sum two numbers
def add(a, b):
    return a + b


if __name__ == "__main__":
    print("Factorial of 5 is: ", factorial(5))
    print("Sum of 5 and 6 is: ", add(5, 6))
