import calc4
import re

valuein = input("Enter Expression-:")
valuelst = re.split(r"(\(|\))", valuein)

def convert(x):
    r = ""
    for i in x:
        r += i
    
    return r


def search(x, y):
    lst = []
    for i in range(len(x)):
        if x[i] == y:
            lst.append(i)

    return lst


for i in valuelst:
    if i == "":
        valuelst.remove(i)

n = 0
m = 0
exitcode = 0

for i in valuelst:
    if i =="(":
        n += 1

for i in valuelst:
    if i ==")":
        m += 1

print(n, m, sep = " | ")


lst_d1 = search(valuelst, "(")
lst_d2 = search(valuelst, ")")

#print(valuelst)
#print(lst_d1)
#print(lst_d2)




#print(valuelst)