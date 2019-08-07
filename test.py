a = int(input())
b = int(input())
c = int(input())
i = 0
if a == b == c:
    print(3)
if a == b or a == c or b == c:
    print(2)
else:
    print(0)

