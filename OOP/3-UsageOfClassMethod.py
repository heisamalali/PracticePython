class Book:
    TYPES = ("A","B")
    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    @classmethod
    def create_book_type_a(cls,name,weight):
        return cls(name,cls.TYPES[0],weight)

    @classmethod
    def create_book_type_b(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)


book1 = Book.create_book_type_a("book name",100)
