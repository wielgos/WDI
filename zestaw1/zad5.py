A = int(input())

b = A / 2
e = 0.0001
for i in range(0, 100):
    b = (b + A / b) / 2
    if b - A / b <= e:
        break
print(b)
