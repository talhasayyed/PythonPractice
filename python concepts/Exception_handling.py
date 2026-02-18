

a = 5
b = 2
# try divide by 0 instead of 2

try:
    print('!!!resource open')
    print(a/b)
    k = int(input("Enter Number "))
# try inputting string insted of Number

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print('Invalid Input, ',e)

except Exception as e:
    print('Something went wrong',e)

finally:
    print('!!!resource closed')