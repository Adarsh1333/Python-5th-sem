a, b, c, d = map(int, input().split())

result = a * b * c * d
result_str = str(result)


if len(result_str) == 1:
    print("0" + result_str)  
else:
    print(result_str[-2] + result_str[-1])
