
###     Read file
# open(file, mode, buffering, encoding, error, newline, closefd, open)

# f = open('abc','r')
# print(f.read())

# or
# for i in f:
#     print(i)



###     Write in File
# f = open('abc','w')
# f.write('something')


###     append in file
# append will look for file if not created then create it
# f = open('abc','a')
# f.write('something')


###     copy one file to another
# f = open('abc','r')
# f2 = open('abc2','a')
#
# for data in f:
#     f2.write(data)