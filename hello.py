n = int(input())
print(n,'$', 'this is the number that you just typed', 'ahihi', 'is this your dream salary')
x = 0
while n >0:
    x = x * 10 + n % 10
    n //= 10
print(x)