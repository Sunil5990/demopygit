def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

print("Enter the length of List: ",end="")
n = int(input())
lst=[]
for i in range(1,n+1):
    print("enter the value No",i,": ",end="")
    lst.append(int(input()))

even,odd = count(lst)
print("Even : {} and odd : {}".format(even,odd))