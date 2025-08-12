n = int(input())
print(n,'$', 'this is the number that you just typed', 'ahihi', 'is this your dream salary')
#version 3 update
#nhap thong tin theo yeu cau va in ra thong tin
print('nhap vao 3 muc thong tin:')
a = {}
while n > 0:
    s = str(input())
    s1 = str(input())
    a[s] = s1
    n -= 1
for x, y in a.items():
    print(x, ': ', y)

    