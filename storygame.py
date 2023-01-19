answer = input("do you like camping?")

if answer == "yes":
    
    print("wow its awesome")
    print()
    answer = input("do you want to go K2 or Nangaparbat?[K2/nanghaparbat]")

    if answer == "K2":
        print("there you can stuck because of bad weather")
        print()
        answer = input("can you live without food and  oxygen ?[food/oxygen]")
        
        if answer =="food":
            print("its impossible,you will die")
          
        elif answer == "oxygen" :
            print("are you insane,its impossible")

        else:
            print("error.you can stay home")   

    elif answer == "nanghaparbat": 
          print("Because of bad weather,NO permission!")

    else:
          print("error.you can stay home")   
else:
    print("you than going to paradise")
