a = [1, 2, 3, 7, 8, 9, 13, 14, 15]
b = [4, 5, 6, 10, 11, 12, 16, 17, 18, 19, 20]
c = []

ai = 0
bi = 0

while ai < len(a) and bi < len(b):
    if a[ai] < b[bi]:
         c.append(a[ai])
         ai += 1
    else:
         c.append(b[bi])
    
while ai < len(a):
     c.append(a)

while bi < len(b):
     c.append(b)

print(c)
