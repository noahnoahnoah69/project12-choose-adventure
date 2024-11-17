name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go (left/right)? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. What would you like to do (walk/swim)? ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You went back and lost.")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talked to the stranger and they gave you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and they were offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you for trying, {name}")
