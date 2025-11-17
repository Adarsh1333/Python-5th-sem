s = input()
for op in '+-*/':
    if op in s:
        a, b = map(int, s.split(op))
        print(a + b if op=='+' else
              a - b if op=='-' else
              a * b if op=='*' else
              a // b)
        break
