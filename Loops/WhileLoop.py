number = 7
while True:
    wouldYouLikeToPlay = input("Would you like to play it (Y/n)?")
    if wouldYouLikeToPlay == "n":
        break
    userNumber = int(input("Enter your number: "))
    if userNumber == number:
        print("You are right!")
    elif number - userNumber in (-1,1):
        print("you are off by one")
    else:
        print("you are wrong")