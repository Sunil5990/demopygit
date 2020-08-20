# Close the file before exit if open it in between
# Close the DB Connection before exit if open it in between
a=5
b=0

try:
    print("Resource Open")
    print(a/b)
    k=int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print("ZeroDivisionError: ",e)

except ValueError as e:
    print("ValueError: ",e)

except Exception as e:
    print("Exception Error: ",e)

finally: #Executes in both cases either try run or except block runs
    print("Resource Closed")