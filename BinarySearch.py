pos=-1

def BinarySearch(list,n):
    l = 0
    u = len(list) - 1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
n=int(input("Enter a number for binary Search:"))
list=[4,7,8,12,45,99]
if BinarySearch(list,n):
    print(n,"Found at",pos+1)
else:
    print("Oops! Not found in the list")