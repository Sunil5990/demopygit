def person(name,**kw): #KWArgs are of Dictionary class
    print(name)
    print(kw)
    print(type(kw))
    for i,j in kw.items():
        print(i,j)


person('Sunil', age=28,  city='Mathura', MobNum=9711042464)