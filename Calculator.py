def evalu(x):
    while '*' in x or '/' in x or '+' in x or '-' in x[1: ]:
        if '*' in x:
            first,last=0,len(x)-1
            mid=x.index('*')
            tempmid=mid-1
            while tempmid!=-1:
                if x[tempmid]=='-' and tempmid!=0 and x[tempmid-1] not in '1234567890':
                    first=tempmid
                    break
                elif x[tempmid]=='-' and tempmid==0:
                    first=tempmid
                    break
                elif x[tempmid] not in '1234567890.':
                    first=tempmid+1
                    break
                tempmid-=1
            tempmid=mid+1
            while tempmid!=len(x):
                if x[tempmid]=='-' and tempmid==mid+1:
                    tempmid+=1
                    continue
                elif x[tempmid] not in '1234567890.':
                    last=tempmid-1
                    break
                tempmid+=1
            num=[x[first:mid],x[mid+1:last+1]]
            c=float(num[0])*float(num[1])
            x=x[ :first]+str(c)+x[last+1: ]
        elif '/' in x:
            first,last=0,len(x)-1
            mid=x.index('/')
            tempmid=mid-1
            while tempmid!=-1:
                if x[tempmid]=='-' and tempmid!=0 and x[tempmid-1] not in '1234567890':
                    first=tempmid
                    break
                elif x[tempmid]=='-' and tempmid==0:
                    first=tempmid
                    break
                elif x[tempmid] not in '1234567890.':
                    first=tempmid+1
                    break
                tempmid-=1
            tempmid=mid+1
            while tempmid!=len(x):
                if x[tempmid]=='-' and tempmid==mid+1:
                    tempmid+=1
                    continue
                elif x[tempmid] not in '1234567890.':
                    last=tempmid-1
                    break
                tempmid+=1
            num=[x[first:mid],x[mid+1:last+1]]
            c=float(num[0])/float(num[1])
            x=x[ :first]+str(c)+x[last+1: ]
        elif '+' in x:
            first,last=0,len(x)-1
            mid=x.index('+')
            tempmid=mid-1
            while tempmid!=-1:
                if x[tempmid]=='-' and tempmid!=0 and x[tempmid-1] not in '1234567890':
                    first=tempmid
                    break
                elif x[tempmid]=='-' and tempmid==0:
                    first=tempmid
                    break
                elif x[tempmid] not in '1234567890.':
                    first=tempmid+1
                    break
                tempmid-=1
            tempmid=mid+1
            while tempmid!=len(x):
                if x[tempmid]=='-' and tempmid==mid+1:
                    tempmid+=1
                    continue
                elif x[tempmid] not in '1234567890.':
                    last=tempmid-1
                    break
                tempmid+=1
            num=[x[first:mid],x[mid+1:last+1]]
            c=float(num[0])+float(num[1])
            x=x[ :first]+str(c)+x[last+1: ]
        elif '-' in x[1: ]:
            first,last=0,len(x)-1
            z=x[1: ]
            mid=z.index('-')+1
            tempmid=mid-1
            while tempmid!=-1:
                if x[tempmid]=='-' and tempmid!=0 and x[tempmid-1] not in '1234567890':
                    first=tempmid
                    break
                elif x[tempmid]=='-' and tempmid==0:
                    first=tempmid
                    break
                elif x[tempmid] not in '1234567890.':
                    first=tempmid+1
                    break
                tempmid-=1
            tempmid=mid+1
            while tempmid!=len(x):
                if x[tempmid]=='-' and tempmid==mid+1:
                    tempmid+=1
                    continue
                elif x[tempmid] not in '1234567890.':
                    last=tempmid-1
                    break
                tempmid+=1
            num=[x[first:mid],x[mid+1:last+1]]
            c=float(num[0])-float(num[1])
            x=x[ :first]+str(c)+x[last+1: ]
    if '+' not in x and '-' not in x[1: ] and '*' not in x and '/' not in x:
        return x
while True:
    x=input(':')
    bracde=list()
    bracde.append(x)
    indlist=list()
    while '(' in bracde[0]:
        if '(' in bracde[-1]:
            braccount=0
            bracnum=bracde[-1]
            bracind=bracnum.index('(')
            for i in range(bracind+1,len(bracnum)):
                if bracnum[i]=='(':
                    braccount+=1
                if bracnum[i]==')' and braccount==0:
                    bracde.append(bracnum[bracind+1:i])
                    indlist.append([bracind,i])
                    break
                if bracnum[i]==')':
                	   braccount-=1
        else:
            ans=evalu(bracde[-1])
            pre=bracde[-2] 
            bracde[-2]=pre[ :indlist[-1][0]]+str(ans)+pre[indlist[-1][1]+1: ]
            bracde.pop(-1)
            indlist.pop(-1)
    lastans=evalu(bracde[-1])
    print(lastans)