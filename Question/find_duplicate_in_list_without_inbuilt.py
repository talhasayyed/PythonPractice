numbers = [1, 2, 3, 2, 4, 5, 1]
seen = set()
duplicates = []

for num in numbers:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print(set(duplicates)) # Output: {1, 2}
