def calc(input):
    import re

    lst = re.split(r"(\D)", input)
    #print(lst)
    for i in lst:
        if i == "":
            lst.remove(i)

    for i in lst:
        if i == ".":
            d = lst.index(i)
            
            string = lst[d-1] + lst[d] + lst[d+1]
            new = float(string)
            lst.insert(d-1, new)
            del lst[d:d+3]
    for i in lst:

        d = lst.index(i)

        if type(i) == str:
            #print(i)
            if i.isdigit():
                #print(i)
                j = int(i)
                lst.insert(d, j)
                del lst[d+1]
            else:
                continue


    for i in lst:
        if i == "-" and str(lst[lst.index(i)-1]) in "+-*/":
            d = lst.index(i)
            new = 0 - lst[d+1]
            lst.insert(d+2, new)
            #print(lst)
            del lst[d:d+2]
            #print(d)

        else:
            continue

    #print(lst)

    for i in lst:
        if i =="-":
            d = lst.index(i)
            n1 = lst[d+1]
            new = 0 - n1
            lst[d] = "+"
            lst.insert(d+1, new)
            del lst[d+2]

    for i in lst:
        if i == "*" or i == "/":
            d = lst.index(i)
            j = lst[d+1]
            if j =="*" or j =="/":
                new = i + j
                lst[d] = new
                del lst[d+1]


    for i in lst:
        if i == "":
            lst.remove(i)


    
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



            
    
    print("Output-: ", lst[0])

value = input("-: ")
calc(value)
print("Eval-: " ,eval(value))