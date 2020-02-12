token_list=["horse","donkey","unicorn","zebra"]
am_money =int(input("how much money do you want to play with? "))
while am_money > 10 or am_money < 1:
    print("You can't play with less then $1 or more than $10")
    am_money =int(input("how much money do you want to play with? "))       
else:
    print("Ok, let's get started!")
    
    
