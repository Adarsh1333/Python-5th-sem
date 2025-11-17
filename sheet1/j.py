num=input()
a,b=num.split()
if int(a)%int(b)==0 or int(b)%int(a)==0:
    print( "Multiples" )
else:
    print("No Multiples" )