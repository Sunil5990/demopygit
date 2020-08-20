

a=10
print(id(a))
def something():
    #global a
    a=9
    x=globals()['a']
    print(id(x))
    globals()['a']=15
    print("In Fun" , a)


something()
print("Outside ", a)