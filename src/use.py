n = int(input())
def git(n):
    if n <= 0:
        return 0
    return n % 10 + git(n // 10)

print(git(n), 'ahihi', 'tong chu so')

print('version 6 cho viec check hoat dong cua github')