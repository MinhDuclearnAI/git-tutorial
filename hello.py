print('nhap vao 3 muc thong tin:')
a = {}
while n > 0:
    s = str(input())
    s1 = str(input())
    a[s] = s1
    n -= 1
for x, y in a.items():
    print(x, ': ', y)

#version7
a = list(map(int, input('version 7 ahihi').split()))
a = set(a)
print(a)

    