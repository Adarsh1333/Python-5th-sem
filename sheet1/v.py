num = input()
a, s, b = num.split()

if s == '<':
    if int(a) < int(b):
        print("Right")
    else:
        print("Wrong")
elif s == '>':
    if int(a) > int(b):
        print("Right")
    else:
        print("Wrong")
else:
    if int(a) == int(b):
        print("Right")
    else:
        print("Wrong")
