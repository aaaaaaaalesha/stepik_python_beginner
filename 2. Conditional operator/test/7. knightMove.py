x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (abs(y1 - y2) == 1 and abs(x2 - x1) == 2) or (abs(y1 - y2) == 2 and abs(x2 - x1) == 1):
    print("YES")
else:
    print("NO")