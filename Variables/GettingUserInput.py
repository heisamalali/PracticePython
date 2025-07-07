import math
# link for course https://git.ir/udemy-mastering-rest-apis-with-fastapi-2/
name = input("What is your name?")
print(name)

area = input("Enter the area of your square: ")
areaInt = int(area)
lengthInt = math.sqrt(areaInt)
print(f"The square side is: {lengthInt:.2f}")