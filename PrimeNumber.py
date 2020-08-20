Num = int(input("Enter a number: "))
for i in range(2,Num//2):
    if Num % i == 0:
        print(Num, " is not a prime number")
        break
else:
    print(Num," is a prime number")