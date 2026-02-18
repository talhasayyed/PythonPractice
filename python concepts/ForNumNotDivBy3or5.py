# python program for number not divisible by 3 or 5
# continue
for num in range(1, 50):
    if num % 3 == 0 or num % 5 == 0:
        continue

    else:
        print(num)