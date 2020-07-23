import calc5
from re import split

exp = "2+(3*(5/(2-1)+2))"

exp_ = split(r"(\(|\))", exp)

for i in exp_:
    if i == "":
        exp_.remove(i)

exitcode = 0

def check(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

z = 1

while exitcode == 0:
    print("-->" ,z)
    z +=1
    if z > 10:
        break

    if ("(" not in exp_) and (")" not in exp_):
        print("True")
        exp_final = ""
        for i in exp_:
            exp_final += str(i)

        print(exp_final)
        final = calc5.calc(exp_final)
        break


    for i in exp_:
        d = exp_.index(i)
        if check(i) is True:
            
            n1 = exp_[d -1]
            n2 = exp_[d+1]

            print(n1, n2)
            if n1 == "(" and n2 == ")":
                del exp_[exp_.index(n1)]
                del exp_[exp_.index(n2)]

            elif n1 == "(" and type(n2) == str:
                i_ = str(i) + n2
                new = calc5.calc(i_)
                exp_[d] = new
                del exp_[d+1]

            elif type(n1) == str and n2 == ")":
                i_ = n1 + str(i)
                new = calc5.calc(i_)
                exp_[d] = new
                del exp_[d-1]
            
            elif type(n1) == str and type(n2) == str:
                i_ = n1 + str(i) + n2
                new = calc5.calc(i_)
                exp_[d-1] = new
                del exp_[d:d+2]
            else:
                continue
        elif type(i) == str:
            n = len(i)

            if (n> 1) and i[0].isdigit() and i[n-1].isdigit():
                new = calc5.calc(i)
                exp_[d-1] = new
                del exp_[d:d +2]
                print(i)
                
            elif (n>1):
                continue

    print(exp_)


print(final)
print(eval(exp))