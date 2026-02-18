# find the max score of out(*)players and not out players show there score with name

# library for url
import requests

r = requests.get("http://localhost/talha/cricket.txt")
s = r.text
# print("actual string is",s)

# crating empty dictionay
d = {}
lines = s.split("\n")
# list of sting splitted by new line
# print(lines)

for line in lines:
    (key,val) = line.split(" |")
    d[(key)] = val
# print(d)
# print(d.keys())
# print(d.values())

# empty dictionary for Out and Not Out players
out = {}
NotOut = {}

for (key,values) in d.items():
    if values[-1]=="*":
        values = int(values[:-1])
        # print(int(values))

        key_value = (key,values)
        out.update({key:values})
    else:
        values = int(values)
        NotOut.update({key:values})

print(d)

print("====================================================")
print("out",out)

for key,values in out.items():
    if values == max(out.values()):
        print("------> max ",key,values)

print("====================================================")
print("NotOut",NotOut)
for key,values in NotOut.items():
    if values == max(NotOut.values()):
        print("------> max ",key,values)
