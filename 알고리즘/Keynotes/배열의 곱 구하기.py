from functools import reduce

arr = [1,2,3,4,5]

def multiply (arr):
    return reduce (lambda x,y: x*y, arr)

print(multiply(arr))

multiply2 = lambda x,y: x*y,arr

print(multiply2(arr))