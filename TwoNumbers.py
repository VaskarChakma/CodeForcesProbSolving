import math
A, B = input().split()
A = int(A)
B = int(B)

print(f"floor {A} / {B} = {math.floor(A/B)}")
print(f"ceil {A} / {B} = {math.ceil(A/B)}")
print(f"round {A} / {B} = {round(A/B)}")