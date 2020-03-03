import random
print("Hello, welcome to the 'Lucky Unicorn' game. Here you can have one of 4 randomly generated tokens: ")
print("unicorn, horse, zebra or donkey and you can win $5, lose 50c or lose $1 respectively.")
print("This game is for raising money for the charity 'Doctors without Borders'.")
print("You should give some money to play with and you can't play with more than $10, because we don't want you to lose a lot of money")
# creating a list of our tokens
tokens = ["horse", "donkey", "unicorn", "zebra"]


# setting up ending system that checks if the total amount is more than or equals $1
def end(a, d):
    if a >= 1:
        if d == "c":        # if user wants to continue calling the function of testing system
            testn(a)        # run the testing function
        else:
            print("Thank you for playing!")
            print("Your balance is $" + str(a))
    else:
        print("Sorry, you have not enough money to play")


# setting up winning system that checks what token did user get and how much money did they win or lose
def win_syst(x):
    token_choice = random.choice(tokens)        # randomly choosing a token from our list
    print("Your token is " + token_choice)
    if token_choice == "unicorn":               # if the token is unicorn add $5 to the total amount
        print(" ")
        print("Congratulations, you won $5!")
        x = x + 5
        print(" ")
        print("Now your balance is $" + str(x))
    elif token_choice == "horse":               # if the token is horse subtracting 50c from the total amount
        print(" ")
        print("Sorry, you lost 50c")
        print(" ")
        x = x - 0.5
        print("Now your balance is $" + str(x))
    elif token_choice == "zebra":               # if the token is zebra subtracting 50c from the total amount
        print(" ")
        print("Sorry, you lost 50c")
        print(" ")
        x = x - 0.5
        print("Now your balance is $" + str(x))
    elif token_choice == "donkey":               # if the token is donkey subtracting $1 from the total amount
        print(" ")
        print("Sorry, you lost $1")
        print(" ")
        x = x - 1
        print("Now your balance is $" + str(x))
    finish = str(input("Press c to continue or any other key to quit "))   # asking user if they want to continue
    end(x, finish)                        # run the function of ending system


# setting up the testing system that checks if user wrote an integer between 1 and 10
def test():
    try:
        print(" ")
        am_money = int(input("how much money do you want to play with? "))   # asking user how much money they want to play with and putting it as integer
        while am_money > 10 or am_money < 1:                                 # if it's not between 1 and 10 print an error message and ask again
            print("You can't play with less then $1 or more than $10")
            print(" ")
            am_money = int(input("how much money do you want to play with? "))
        else:
            print(" ")
            print("Ok, let's get started!")
            win_syst(am_money)                                    # run winning system

    except:                              # if it's not integer print an error message and try again
        print("Please write an integer")
        test()                           # run this exact function again


# noinspection PyBroadException
# setting up a testing system for the ending that checks if user put an integer between 0 and 10
def testn(m):
    try:
        b = int(input("How much do you want to add to your balance? "))   # asking how much the user wants to add and putting it as an integer
        while b > 10 or b < 0:                 # if it's not between 0 and 10 print an error and ask again
            print("You cant add less than $0 or more than $10")
            b = int(input("How much do you want to add to your balance? "))
        else:
            m = m + b    # adding the money user added to the total amount
            print("Your balance is $" + str(m))
            m = int(m)   # converting total to integer
            print("Ok, lets continue!")
            win_syst(m)    # running winning system
    except:
        print("Please write an integer")
        testn(m)         # running this function again


test()   # running testing function
