inp=input()
a=eval(inp)
a_kopie=[]

n1=len(a)
n2=len(a[0])
for i in range(n1):
    a_kopie.append([])
for i in range(n1):
    for j in range(n2):
        a_kopie[i].append(a[i][j])
n=len(a)

for i in range(n1):
    for j in range(n2):
        zivot=0
        for o in range(-1,2):
            for k in range(-1,2):
                first=(i+o)
                second=(j+k)
                if first!=-1 :
                    first=first%n1
                if second!=-1:
                    second=second%n2
                if a[first][second]==1 and (first!=i or second!=j):
                    zivot+=1
        if zivot<2:
            a_kopie[i][j]=0
        elif zivot==2:
            if(a_kopie[i][j]!=0):
                a_kopie[i][j]=1
        elif zivot==3:
            a_kopie[i][j]=1
        else:
            a_kopie[i][j]=0

print(a)
print(a_kopie)