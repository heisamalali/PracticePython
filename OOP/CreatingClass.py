class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


student1 = Student('Ali', 35)
print(student1.get_name())