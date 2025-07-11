class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # __ methods called magic methods
    # when we try to print the object .toSting() will be called
    def __str__(self):
        return f'Student {self.name}, age: {self.age}'

    def __repr__(self):
        return f'Student {self.name}, age: {self.age}'
    def get_name(self):
        return self.name



student1 = Student('Ali', 35)
print(student1.get_name())