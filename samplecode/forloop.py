ls=[1,'abc',{'hello', 'world'}]

# part1
print("part1:")
for item in ls:
    print(item)

# part2
print("part2:")

临时迭代器=iter(ls)
状态=True

while 状态:
    try:
        item=next(临时迭代器)
    except StopIteration:
        状态=False
    else:
        print(item)

# part3
print("part3:")

临时索引=0
状态=True

while 状态:
    try:
        item=ls[临时索引]
    except IndexError:
        状态=False
    else:
        print(item)
        临时索引+=1