# n = 4
# count = 0
# maximum = 999
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = i
#             break
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

count = 0
maximum = 0
for _ in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
