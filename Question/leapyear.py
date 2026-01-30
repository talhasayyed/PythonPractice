# leap year

def leapyear(year):
    leap = False
    # year divisible by 400
    if year % 400 == 0:
        leap= True
    # year not divisible by 100
    elif year % 100 != 0:
        leap= False
    # year divisible by 4
    elif year % 4 == 0:
        leap= True
    return leap


yr = int(input("enter year: "))
print(leapyear(yr))
