def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    print(total)
    return total

multiply(1,2,3,4,5)

def add(a,b):
    return a+b

numbers = [1,2]
print(*numbers)
add_result = add(*numbers)
print(add_result)
