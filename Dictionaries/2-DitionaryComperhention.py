users = [
    (0,"Bob","BobPassword"),
    (1,"Smith","SmithPassword"),
]

username_mapping = {user[1]:user for user in users}
print(username_mapping)