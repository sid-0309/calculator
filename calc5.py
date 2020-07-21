def calc(inp):
    import re

    inp_temp = ""

    exitcode1 = 0

    while exitcode1 == 0:
        if "--" in inp:
            inp_temp = inp.replace("--", "+")
            inp = inp_temp
            inp_temp = ""

        elif "++" in inp:
            inp_temp = inp.replace("++", "+")
            inp = inp_temp
            inp_temp = ""

        elif "+-" in inp:
            inp_temp = inp.replace("+-", "-")
            inp = inp_temp
            inp_temp = ""

        elif "-+" in inp:
            inp_temp = inp.replace("-+", "-")
            inp = inp_temp
            inp_temp = ""

        else:
            exitcode1 = 1

    lst = re.split(r"(\D)", inp)

    print(lst)

    for i in lst:
        if i == "":
            lst.remove(i)

    for i in lst:
        d= lst.index(i)

        if i == ".":
            n1 = lst[d-1]
            n2 = lst[d+1]
            print(n1)
            print(n2)

            new_str = n1 + i + n2
            new1 = float(new_str)

            lst[d+1] = new1
            del lst[d-1:d+1]

    for i in lst:

        d = lst.index(i)


        if i == "-":
            if d == 0:
                n1 = float(lst[d+1])
                new = 0 - n1
                lst[d+1] = new
                del lst[d]

            elif d > 0:
                n1 = float(lst[d+1])
                new = 0 - n1
                lst[d+1] = new
                lst[d] = "+"

    for i in lst:
        if i == "*" or i == "/":
            d = lst.index(i)
            j = lst[d+1]
            if j =="*" or j =="/":
                new = i + j
                lst[d] = new
                del lst[d+1]



    for i in lst:
        d = lst.index(i)
        if type(i) == str:
            if i.isdigit():
                new3 = float(i)
                lst[d] = new3


    for i in lst:
        if i == "":
            lst.remove(i)

    print(lst)

    exitcode = 0
    a = "**"
    #print(lst)



    while exitcode == 0:
        if a in lst:
            d = lst.index(a)
            n1 = float(lst[d-1])
            n2 = float(lst[d+1])
            
            if a == "+":
                new = n1 + n2

            elif a == "*":
                new = n1 * n2
            elif a == "/":
                new = n1 / n2
            elif a == "**":
                new = n1 ** n2
            elif a == "//":
                new = n1 // n2
            else:
                print("ERROR1")
                break

            #print(n1, a, n2, new, sep = " | ")
            #print(lst)
            lst.insert(d-1, new)
            del lst[d:d+3]




        elif a == "**" and a not in lst:
            a = "//"

        elif a == "//" and a not in lst:
            a = "/"
        elif a == "/" and a not in lst:
            a = "*"
        elif a == "*" and a not in lst:
            a = "+"


        else:
            for i in ["+", "*", "/"]:
                if i not in lst:
                    exitcode = 1


    #print("Output = ", lst[0])
    return lst[0]

exp = input("--:")

calc(exp)
print("Eval output = ", eval(exp))