import random

# Generate 100 random integers
random_numbers = [random.randint(1, 100) for _ in range(100)]

print('Random Numbers:')
print(random_numbers)

# Filter odd numbers
odd_numbers = [num for num in random_numbers if num % 2 != 0]

print('\nOdd Numbers:')
print(odd_numbers)