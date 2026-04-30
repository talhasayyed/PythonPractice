from collections import Counter

numbers = [1, 2, 3, 2, 4, 5, 1]
counts = Counter(numbers)
duplicates = [item for item, count in counts.items() if count > 1]

print(duplicates) # Output: [1, 2]
