x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0) or ((x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0):
    print("YES")
else:
    print("NO")