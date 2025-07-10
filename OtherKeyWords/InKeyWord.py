friends = ["Bob", "Smith"]
print("Bob" in friends)
yourName = input("What is your name? ")
if yourName in friends:
    print("Yes")
else:
    print("No")

number = 7
wouldYouLikeToPlay = input("If you would like to play enter y")
if wouldYouLikeToPlay in ("y","Y"):
    userNumber = int(input("Enter your number: "))
    if userNumber == number:
        print("Yes")
    elif number - userNumber in (-1,1):
        print("you are off by one")
    else:
        print("it is not true")
else:
    print("you don't want to play it")