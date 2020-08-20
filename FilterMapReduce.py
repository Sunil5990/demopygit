from functools import reduce
# Use of lamdba Fn (Anonymous Fn)
nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n: n % 2 == 0, nums))

doubles = list(map(lambda n: n*2, evens))
print(evens)
print(doubles)

sum = reduce(lambda a,b: a+b , doubles)

print(sum)