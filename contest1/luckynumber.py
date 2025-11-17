num=input()

A,B=(map(int,num))
#print (A, B)
if 0 in (A, B):
    print("YES")

elif A%B==0 or B%A==0:
    print("YES")
else:
    print("NO")