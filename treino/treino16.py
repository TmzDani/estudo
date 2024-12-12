a = [1, 3,3,3.3, 5, 7, 9]
b = [2,2,2,2, 4, 6, 8, 10, 11, 12, 13, 14]
c = []

for i in range(max(len(a), len(b))):
    if i < len(a):
        c.append(a[i])
    if i < len(b):
        c.append(b[i])
print(c)
