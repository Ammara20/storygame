#After working late hours going home thats near my work place,its a rainy day and street is full of water.During walking i didnt saw hole and fell down.#

#level1
level1_done = False

while level1_done == False:
    print("what do you do?(LOOK/SHOOT/MOVE)")
    choice = input() 
    if choice == "LOOK":
        print("You look around, but its too dark to see.")
        print("USE FLASHLIGHT? (Y/N)")
        sub_choice = input()
        if sub_choice == "Y":
            print("There is the exit, go!")
            level1_done = True
        else:
            print("Man your really cant see anything")
    elif choice == "SHOUT":
        print("No one replies")
    elif choice == "MOVE":
        print("You moved without seeing but your feel light in front of you!")
        level1_done = True
    else:
        print("Invalid input. You better make a decision..")



#level2
print("level2")
level2_done = True
while level2_done == True:
    print("what is more possibilty to get out in from hole?(FINDING/DIE/LIFE")   
    choice = input() 
    if  choice == "FINDING":
         print("searching bag to find mape or something more")
         print("using mape and compex ?(Y/N)")
         sub_choice = input()
         if sub_choice == "Y":
            print("There is the exit, go!")
            level2_done = True
         else:
            print("There is no way out,Die")
         
    elif choice == "DIE":
        print("just watching yourself die")
        level2_done = True
    elif choice == "LIFE":
        print("Iphone helpline get help to out!")
        level2_done = True
    else:
        print("Never go to cave without iphone")
