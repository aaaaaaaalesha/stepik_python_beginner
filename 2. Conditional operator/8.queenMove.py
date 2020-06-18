x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (abs(y1 - y2) == abs(x2 - x1)) or (x1 == x2 or y1 == y2):
    print("YES")
else:
    print("NO")