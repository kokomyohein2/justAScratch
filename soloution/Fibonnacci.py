a = 1
b = 0
print(b)
for i in range(10):
    a, b = a + b, a
    print(a)
