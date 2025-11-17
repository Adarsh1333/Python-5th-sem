A, S, B, Q, C = input().split()

A = int(A)
B = int(B)
C = int(C)

# compute the correct answer
if S == '+':
    result = A + B
elif S == '-':
    result = A - B
else:  # S == '*'
    result = A * B

# compare result with given C
if result == C:
    print("Yes")
else:
    print(result)
