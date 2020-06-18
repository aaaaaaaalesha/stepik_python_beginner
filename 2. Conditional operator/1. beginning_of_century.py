y = int(input())

if (y % 10 == 0) and (y // 10 % 10 == 0):
    print("YES")
else:
    print("NO")