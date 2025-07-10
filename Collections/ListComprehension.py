numbers = [1,2,3]
doubleNumbers = [x*2 for x in numbers]
print(doubleNumbers)

friends = ["Hoda","Samir","Sara","Soheil"]
friendsWith_S = [friend for friend in friends if friend.startswith("S")]
print(friendsWith_S)