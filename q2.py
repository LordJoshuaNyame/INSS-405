import random

def sort_numbers(numbers):
    # Bubble sort algorithm
    n = len(numbers)
    for i in range(n):
        for x in range(0, n-i-1):
            if numbers[x] > numbers[x+1]:
                numbers[x], numbers[x+1] = numbers[x+1], numbers[x]

#Generate 100 random numbers
random_numbers = [random.randint(1, 1000) for _ in range (100)]

print('Random Numbers (before sorting):')
print(random_numbers)

#Sort the numbers
sort_numbers(random_numbers)

print('\nSorted Numbers:')
print(random_numbers)