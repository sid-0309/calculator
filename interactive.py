def calc(inp):
    from re import split


    exitcode1 = 0

    while exitcode1 == 0:
        inp_temp = inp.replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-").replace("**","^").replace("//", "$")

        inp = inp_temp

        for  i in ["++", "--", "+-", "-+"]:
            if i not in inp:
                exitcode1 = 1


    lst = split(r"(\+|\-|\/|\*|\^|\$)", inp)


    for i in lst:
        if i == "":
            lst.remove(i)



    for i in lst:


        d = lst.index(i)


        if i == "-":
            if (d == 0) or (lst[d-1] in "*/"):
                new = 0 - float(lst[d+1])
                lst[d+1] = new
                del lst[d]

            elif (lst[d-1] not in "*/") or (d > 0):
                new  = 0 - float(lst[d+1])
                lst[d+1] = new
                lst[d] = "+"
            



    for i in lst:
        if i == "":
            lst.remove(i)



    def evaluvator(a):
        global lst
        while "+" in a or "*" in a or "/" in a or "$" in a or "^" in a:
            for i in ops.keys():
                if i in a:
                    d=  a.index(i)
                    n1 = float(a[d-1])
                    n2 = float(a[d+1])
                    new =ops[i](n1, n2)

                    a[d-1] = new
                    del a[d:d+2]


        lst = a




    ops = {
        "^":lambda x,y:x**y,
        "$":lambda x,y:x//y, 
        "/":lambda x,y:x/y, 
        "*":lambda x,y:x*y, 
        "+":lambda x,y:x+y
        }

    evaluvator(lst)

    end_output = round(lst[0], 3)

    
    return end_output


print(r"      ____  ____         ____               ____  _____  ____   ____ ")
print(r"     |     |    | |     |     |    | |     |    |   |   |    | |    |")
print(r"     |     |----| |     |     |    | |     |----|   |   |    | |----'")
print(r"     |____ |    | |____ |____ |____| |____ |    |   |   |____| |   | ")


default = ""

while True:
    if default == "":
        print("Enter expression.")
        exp = input()
    else:
        exp = input(output)

  
    if exp == "x":
        break
    elif exp == "c":
        default  = ""
        continue
    else:

        output = calc(str(default) + exp)
        default = output
   
