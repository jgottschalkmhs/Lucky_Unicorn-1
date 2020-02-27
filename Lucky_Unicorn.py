import random
tokens = ["horse", "donkey", "unicorn", "zebra"]

def end(a):
    if a>=1:
        finish = str(input("Press C to continue or any other key to quit "))
        if finish == "c":
            b=1
            try:
                b = int(input("How much do you want to add to your balance? "))
                while b > 10 or b < 0:
                    print("You cant add less than $0 or more than $10")
                    b = int(input("How much do you want to add to your balance? "))
                else:
                    a = a + b
                    print("Your balance is $" + str(a))
                    a = int(a)
                    print("Ok, lets continue!")
                    win_syst(a)
            except:
                print("Please write an integer")
        else:
            print("Thank you for playing!")
            print("Your balance is $" + str(a))

    else:
        print("Sorry, you have no money")


def win_syst(x):
    token_choice = random.choice(tokens)
    print("Your token is " + token_choice)
    if token_choice == "unicorn":
        print(" ")
        print("Congrats, you won $5!")
        x = x + 5
        print(" ")
        print("Now your balance is $" + str(x))
    elif token_choice == "horse" or token_choice == "zebra":
        print(" ")
        print("Sorry, you lost 50c")
        print(" ")
        x = x - 0.5
        print("Now your balance is $" + str(x))
    elif token_choice == "donkey":
        print(" ")
        print("Sorry, you lost $1")
        x = x - 1
        print("Now your balance is $" + str(x))
    end(x)


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

test()
