def calculate_user_age():
    age = int(input("Please enter your age: "))
    if age >= 18:
        print(age)
    else:
        print("Sorry, you are under 18 years old")

calculate_user_age()

def sum_numbers(a,b=5):
    return a+b

result = sum_numbers(a=6,b=8)
print(result)

add_two_numbers = lambda a,b: a+b
result = add_two_numbers(1,2)
print(result)

double_numbers = lambda a: a*2

listOfNumbers = [1,2,3,4,5,6,7,8,9]
double_numbers_by_two = list(map(double_numbers,listOfNumbers))
double_numbers_by_two_new_way=[double_numbers(x) for x in listOfNumbers]
print(double_numbers_by_two)