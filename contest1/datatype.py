n, k, a = map(int, input().split())


if (n * k) % a != 0:
    print("double")
else:
    result = (n * k) // a

    INT_MIN = -2147483648
    INT_MAX = 2147483647

    if INT_MIN <= result <= INT_MAX:
        print("int")
    else:
        print("long long")
