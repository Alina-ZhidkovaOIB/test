
from unittest import result


def factorial(n):
    if n == 0 or == 1:
        return 1
    else:
        return n * factorial(n-1)
def factorials_list(n):
    fact = factorial(n)
    result = []
    whil fact > 0:
        result.append(fact)
        fact //= 2
    return result
number = 3
fact_of_number = factorial(number)
result_list =
factorials_list(fact_of_number)
print(fact_of_number)
print(result_list)
