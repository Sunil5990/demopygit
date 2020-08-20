def update(x):
    print(id(x))
    lst[1] = 25
    print(id(x))
    print("x ",x)

lst = [10, 20, 30]
print(id(lst))
update(lst)
print("lst", lst)

