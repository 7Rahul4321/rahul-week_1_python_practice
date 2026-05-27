#  To add two numbers
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


# second code
def calculations(a, b):
    return a + b, a - b

sum_value, sub_value = calculations(10, 5)

print("Addition:", sum_value)
print("Subtraction:", sub_value)

# third code
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# 4th code
def find_max(numbers):
    return max(numbers)

nums = [4, 7, 2, 9, 1]
print("Largest number:", find_max(nums))
