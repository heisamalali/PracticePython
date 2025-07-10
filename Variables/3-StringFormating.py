name = "Bob"
# we call this f string
greeting = f"Hello {name}"
print(f"Hello {name}")
name = "john"
print(f"Hello {name}")

# with this we can use formating function
anotherGreetingTemplate = "Hello {}"
print(anotherGreetingTemplate.format(name))

anotherTemplate = "Helle {} , I'm {}"
print(anotherTemplate.format("Hamid","Heysam"))