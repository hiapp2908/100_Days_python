print("Welcome to Treasure Hunt!\nYour mission is to find the treasure.")

choice_1 = input("You're at the crossroads where will you go: left or right:\n").lower()
if choice_1 == "left":
    choice_2 = input("Now you reached at the river. Will you swim or wait for the boat:\n").lower()
    if choice_2 == "wait":
        choice_3 = input("You reached safely to a house with 3 doors. red, blue & green. Pick a gate:\n")
        if choice_3 == "blue":
            print("Congratulations! You got the Treasure. YOU WIN!!!!!!!!!!!!!!!")
        else:
            print("You chose the wrong door. You got killed by the watcher of treasure. Try again!")
    else:
        print("You chose the wrong path. You got killed by crocodiles in the river. Try again!")
else:
    print("You chose the wrong path got lost in jungle and killed by wild animals. Try again!")
