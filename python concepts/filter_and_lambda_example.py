import timeit
import random

# Create a sample list
data = list(range(1_000_000))

# Method 1: filter + lambda
def method_filter():
    return list(filter(lambda x: x % 2 == 0, data))

# Method 2: list comprehension
def method_list_comp():
    return [x for x in data if x % 2 == 0]

# Time both methods
time_filter = timeit.timeit(method_filter, number=10)
time_list_comp = timeit.timeit(method_list_comp, number=10)

print(f"Filter + lambda time: {time_filter:.4f} seconds")
print(f"List comprehension time: {time_list_comp:.4f} seconds")

# Oputput
# Filter + lambda time: 0.9166 seconds
# List comprehension time: 0.3774 seconds