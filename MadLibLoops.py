import random

user_state = str(input("State something and then an amount of that!\n"
                       "Example: bannanas 12\n"
                       "Type QUIT 0 to quit!\n"
                       ">"))
user = user_state.split()

if user[0] == '0':
    print("Goodbye!")
    quit()
else:
    pass

while user[0] != "quit" and user[1] != 0:
    phrases = (
        ["Eating", user[1], user[0], "a day keeps the doctor away!"],
        ["Watch out! You're about to step on", user[1], user[0] + "!"],
        ["Your", '{} {}'.format(user[1], user[0]), "are very sticky!"]
        # can add more if wanted
    )

    x = len(phrases)
    ran_num = random.randrange(0, x)
    print(*phrases[ran_num])
    user_state = str(input())
    user = user_state.split()
else:
    print("Goodbye!")
    quit()
