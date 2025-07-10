friends_age = {"Adam":30,"Tim":35,"Bob":40,"Jim":35}
print(friends_age["Adam"])

#we can add a new value to dictionary
friends_age["Smith"] = 40

#we can get the values of dictionary as a list
ages = friends_age.values()
print(ages,sum(ages)/len(ages))

# we can get the keys only
keys = friends_age.keys()
print(keys)

#we can access both in for loop
for key,value in friends_age.items():
    print(key,value)