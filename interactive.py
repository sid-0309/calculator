def calc(inp):
    from re import split
    inp = inp.replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-").replace("**","^").replace("//", "$")
    lst = split(r"(\+|\-|\/|\*|\^|\$)", inp)
    lst = [i for i in lst if i !=""]
    for i in lst:
        if i == "-":
            if (lst.index(i) == 0) or (lst[lst.index(i)-1] in "*/"):
                lst[lst.index(i) +1] = 0 - float(lst[lst.index(i) +1])
                del lst[lst.index(i)]
            elif (lst[lst.index(i)-1] not in "*/") or (lst.index(i) > 0):
                lst[lst.index(i) +1] = 0 - float(lst[lst.index(i)+1])
                lst[lst.index(i)] = "+"
    lst = [i for i in lst if i !=""]
    def evaluvator(a):
        global lst
        while "+" in a or "*" in a or "/" in a or "$" in a or "^" in a or "-" in a:
            for i in ops.keys():
                if i in a:
                    a[a.index(i) -1] = ops[i](float(a[a.index(i) -1]), float(a[a.index(i) +1]))
                    del a[a.index(i):a.index(i) +2]
        lst = a
    ops = {"^":lambda x,y:x**y,"$":lambda x,y:x//y, "/":lambda x,y:x/y, "*":lambda x,y:x*y,"+":lambda x,y:x+y}
    evaluvator(lst)
    return round(lst[0], 3)
def check(a):
    global x
    try:
        x = calc(a)
        return x
    except Exception:
        return False
print(r"      ____  ____         ____               ____  _____  ____   ____ ")
print(r"     |     |    | |     |     |    | |     |    |   |   |    | |    |")
print(r"     |     |----| |     |     |    | |     |----|   |   |    | |----'")
print(r"     |____ |    | |____ |____ |____| |____ |    |   |   |____| |   | ")
print()
print("Enter x to exit.")
print("Enter c to clear.")
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
    else:
        if check(str(default) + exp) is not False:
            output = x
            default = output
        else:
            print("Syntax Error!")
            output, default = str(default), output   