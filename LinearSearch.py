pos=-1
def LinearSearch(list, n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    else:
        return False

list=[5,8,4,6,9,2]
n=int(input("Enter a Number to search: "))
if LinearSearch(list,n):
    print(n,"Found at Position",pos+1)
else:
    print("oops! the number you have entered is not in the list")
