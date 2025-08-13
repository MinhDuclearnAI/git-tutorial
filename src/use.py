n = int(input())
def git(n):
    if n <= 0:
        return 0
    return n % 10 + git(n // 10)

print(git(n), 'ahihi', 'tong chu so')

a = []
n = int(input('version 7 mang 2 chieu'))
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)