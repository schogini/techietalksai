def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(e)