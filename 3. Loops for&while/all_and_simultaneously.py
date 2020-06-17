n = int(input())
cnt3 = 0
cntLD = 0
cntEven = 0
ld = n % 10
sumGr5 = 0
multGr7 = 1
cnt05 = 0

while n > 0:
    x = n % 10

    if x == 3:
        cnt3 += 1

    if x == ld:
        cntLD += 1

    if x % 2 == 0:
        cntEven += 1

    if x > 5:
        sumGr5 += x

    if x > 7:
        multGr7 *= x

    if x == 0 or x == 5:
        cnt05 += 1

    n //= 10

print(cnt3)
print(cntLD)
print(cntEven)
print(sumGr5)
print(multGr7)
print(cnt05)

