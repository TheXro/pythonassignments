# Task 1
result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
print(','.join(result))

# Task 2
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

numbers = [5, 6, 7, 8]
factorials = [str(factorial(num)) for num in numbers]
print(','.join(factorials))

# Task 3
n = 8  # Example value
result_dict = {i: i*i for i in range(1, n+1)}
print(result_dict)

# Task 4
numbers_input = input("Enter comma-separated numbers: ")
numbers_list = numbers_input.split(',')
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)
