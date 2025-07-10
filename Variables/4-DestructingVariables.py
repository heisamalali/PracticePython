x,y = (3,4)
print(x,y)

t = 5,6
x,y = t
print(x,y)

friends_age = {"Bob":30, "Alice":25}
print(list(friends_age.items()))

name,_,age = ("Bob","Alice",25)
print(name,age)

head,*tail = ("Bob","Alice",25)
print(head,tail)
