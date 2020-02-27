import random
print("Hello, welcome to the 'Lucky Unicorn' game. Here you can have one of 4 randomly generated tokens: ")
print("unicorn, horse, zebra or donkey and you can win $5, lose 50c or lose $1 respectively.")
print("This game is for raising money for the charity 'Doctors without Borders'.")
print("You should give some money to play with and you can't play with more than $10, because we don't want you to lose a lot of money")
tokens = ["horse", "donkey", "unicorn", "zebra"]

def end(a,d):
    if a>=1:
        if d == "c":
            testn(a)
        else:
            print("Thank you for playing!")
            print("Your balance is $" + str(a))
    else:
        print("Sorry, you have not enough money to play")


def win_syst(x):
    token_choice = random.choice(tokens)
    print("Your token is " + token_choice)
    if token_choice == "unicorn":
        print(" ")
        print("Congratulations, you won $5!")
        x = x + 5
        print(" ")
        print("Now your balance is $" + str(x))
    elif token_choice == "horse":
        print(" ")
        print("Sorry, you lost 50c")
        print(" ")
        x = x - 0.5
        print("Now your balance is $" + str(x))
    elif token_choice == "zebra":
        print(" ")
        print("Sorry, you lost 50c")
        print(" ")
        x = x - 0.5
        print("Now your balance is $" + str(x))
    elif token_choice == "donkey":
        print(" ")
        print("Sorry, you lost $1")
        print(" ")
        x = x - 1
        print("Now your balance is $" + str(x))
    finish = str(input("Press c to continue or any other key to quit "))
    end(x,finish)


def test():
    try:
        print(" ")
        am_money = int(input("how much money do you want to play with? "))
        while am_money > 10 or am_money < 1:
            print("You can't play with less then $1 or more than $10")
            print(" ")
            am_money = int(input("how much money do you want to play with? "))
        else:
            print(" ")
            print("Ok, let's get started!")
            win_syst(am_money)

    except:
        print("Please write an integer")
        test()


# noinspection PyBroadException
def testn(m):
    try:
        b = int(input("How much do you want to add to your balance? "))
        while b > 10 or b < 0:
            print("You cant add less than $0 or more than $10")
            b = int(input("How much do you want to add to your balance? "))
        else:
            m = m + b
            print("Your balance is $" + str(m))
            m = int(m)
            print("Ok, lets continue!")
            win_syst(m)
    except:
        print("Please write an integer")
        testn(m)

test()
