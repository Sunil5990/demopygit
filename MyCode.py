for i in range(4):
    for j in range(4):
        print ("#", end=" ")
    print()
print()
print("=====================================")
for k in range(5):
    for l in range(k,0,-1):
        print("#", end=" ")
    print()
for k in range(5,0,-1):
    for l in range(k):
        print("#", end=" ")
    print()
print()
print("=====================================")
for k in range(10,0,-1):
    for l in range(k-1):
        print(" ", end="")
    for m in range(10-k+1):
        print("#", end=" ")
    print()
for k in range(1,11,1):
    for l in range(k):
        print(" ", end="")
    for m in range(10,k,-1):
        print("#", end=" ")
    print()