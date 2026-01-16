import sys

def factorial(n):
    if n < 0:
        raise ValueError("Negative number not allowed")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)

    num = int(sys.argv[1])
    print("Factorial:", factorial(num))
