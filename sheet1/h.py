A, B = map(int, input().split())
x = A / B

print(f"floor {A} / {B} = {int(x)}")
print(f"ceil {A} / {B} = {int(x) + (x != int(x))}")
print(f"round {A} / {B} = {int(x + 0.5)}")
