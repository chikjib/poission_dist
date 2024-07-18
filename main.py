"""
POISSON DISTRIBUTION FORMULA
P(X) = e^(-lambda) * lambda^x / x!
"""
import math


def poisson_distribution(lambda_value, x):
    return math.exp(-lambda_value) * (lambda_value**x) / math.factorial(x)


def main():
    lambda_value = float(input("Enter the lambda value: "))
    x = int(input("Enter the value of x: "))
    result = poisson_distribution(lambda_value, x)
    result = round(result * 100, 2)
    print(f"P(X = {x}) = {result}%")


main()