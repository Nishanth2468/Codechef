# calculator.py

import math
import os

# Global variable (bad practice)
result = 0


def add(a, b):
    return a + b


def divide(a, b):
    return a / b   # No zero division handling


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def process_numbers(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]

    avg = total / len(nums)

    return total, avg


def read_file():
    f = open("data.txt", "r")   # File not closed
    data = f.read()
    return data


def unused_function():
    print("This function is never used")


def main():

    numbers = [10, 20, 30, 40]

    total, avg = process_numbers(numbers)

    print("Total:", total)
    print("Average:", avg)

    print("Addition:", add(5, 7))

    print("Division:", divide(10, 0))   # runtime error

    print("Factorial:", factorial(-5))  # infinite recursion

    data = read_file()
    print(data)


main()
