lst = []
max=0
index=0
for i in range(1, 10):
    a=int(input())
    lst.append(a)
    if a > max:
        max = a
        index = i

print(max)
print(index)