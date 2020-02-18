import random
print("Hello, welcome to the 'Lucky Unicorn' game. Here you can have one of 4 randomly generated "+
      "tokens: unicorn, horse, zebra or donkey and you can win $5, lose 50c or lose $1 respectively."+
      "This game is for raising money for the charity Doctors without Borders. You should give some "+
      "money to play with and you can't play with more than $10.")
tokens=["horse","donkey","unicorn","zebra"]

def win_syst(x):
    if token_choice == "unicorn":
        print("Congrats, you won $5!")
        x = x + 5
        print("Now your balance is $" + str(x))
    elif token_choice == "horse" or token_choice == "zebra":
        print("Sorry, you lost 50c")
        x = x - 0.5
        print("Now your balance is $" + str(x))
    elif token_choice == "donkey":
        print("Sorry, you lost $1")
        x = x - 1
        print("Now your balance is $" + str(x))
    end(x)


def end(a):
    if a>1:
        finish = input("Press Q for quit or C to continue ")
        if finish == "C" or "c":
            print("Your balance is $" + str(a))
            b = int(input("How much do want to add to your balance? "))
            a = a+b
            while a > 10:
                print("You can't play with more than $10")
                a =int(input("How much do want to add to your balance? "))       
            else:
                print("Ok, let's continue!")
                token_choice = random.choice(tokens)
                print("Your token is " + token_choice)
                win_syst(a)
        elif finish == "q" or "Q":
            print("Game ended")
            print("Your balance is $" + str(a))
            a = 0
        
    else:
        print("Sorry, you have no money")
    


am_money =int(input("how much money do you want to play with? "))
while am_money > 10 or am_money < 1:
    print("You can't play with less then $1 or more than $10")
    am_money =int(input("how much money do you want to play with? "))       
else:
    print("Ok, let's get started!")
    token_choice = random.choice(tokens)
    print("Your token is " + token_choice)
    win_syst(am_money)
    



