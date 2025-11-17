num=input()
#Only one line containing the following space-separated values: int, long long, char, float and double respectively.
a,b,c,d,e=num.split()
print(int(a))
print(int(b))
print(c)
print("{0:.3f}".format(float(d)))
print("{0:.1f}".format(float(e)))