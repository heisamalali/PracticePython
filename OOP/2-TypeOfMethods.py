class Person:

    # for calling instant methods we always need instant
    def instant_method(self):
        print(self)

    # for calling class methods we don't need instant
    # this type of method mostly is used to create instance , a factory
    @classmethod
    def class_method(cls):
        print(cls)

    # this is a static method
    @staticmethod
    def static_method():
        print("this is a static method")