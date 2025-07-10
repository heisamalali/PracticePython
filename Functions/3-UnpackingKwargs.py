def names(**kwargs):
    print(kwargs)

names(name="Ali",age=35)

dictionaryNames = {'name': 'Ali', 'age': 35}

names(**dictionaryNames)