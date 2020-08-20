def square (a):
    return a*a

result = square(5)

print(result)

# if Fn body have only one expression then use lambda exp/lambda Fn
# can pass N no of Variables but lambda Fn can have only one expression
f = lambda a,b : a+b

result = f(5,6)
print(result)