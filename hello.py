from collections import Counter
n = int(input())
print(n, 'this is the number that you just typed', 'ahihi')
#su dung counter version sau version add git ignore
a = list(map(int, input().split()))
b = dict(Counter(a))
print(b)
