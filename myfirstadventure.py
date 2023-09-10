print("You look lost, let me help you try to find your way home, just be careful out here!")
first_name = input("I'm Saria, What's your name?: ")
print(f"Nice to meet you, {first_name.capitalize()}, I hope we can get you out of here, my advice is to think twice before making the wrong turn... these woods are dangerous")
print("Here is some bug spray and a fly swatter, you're going to need it!")
print("You start your adventure out in the woods, it is beautiful and quiet; a little eerie, but it also feels a little familiar...")
print("I will be your guide, am I real? Maybe I am just a voice in your head, you'll never really know!")

while True:
    direction = input(f"What direction would you like to go, {first_name.capitalize()}? (left/right): ").lower()
    if direction in ("left", "right"):
        break  
    else:
        print("Invalid choice. Please choose 'Right' or 'Left'.")
if direction == "left":
    go_swamp = input("You step into a murky swamp...do you go around it to avoid getting stuck? (yes/no): ")
    if go_swamp == "yes":
        print("Good decision!!")
        print("As you continue through the swamp, you find a hidden treasure chest!")
        treasure = input("Do you open the treasure chest? (yes/no): ").lower()

        if treasure == "yes":
            print(f"Congratulations! You've found a chest full of gold coins. You're rich, {first_name.capitalize()}!")
            print("Maybe hang onto that, just incase you make it out of here alive...")
            print("..You continue on your way, and find yourself lost in the woods, but you hear some footsteps...")

            weapon = input("You should probably find something to protect yourself, just in case. What do you grab? (rock/stick): ").lower()
            if weapon in ("rock", "stick"):
                 print("You hold your " +str(weapon) +" close and hope you don't run into some bad characters!")
                

       
        else:print("You decide not to open the chest and continue your adventure.") 
            
             
        convergence_point = input("You continue your journey and eventually arrive at a mysterious cave entrance. You hear a growling behiind you..not knowing what is behind you, or in the cave, do you enter it? (yes/no): ").lower()
        if convergence_point == "yes":
                print("You enter the cave and discover an escape route.")
                print("Congratulations! You've successfully completed your adventure and made it out of here alive!")
                quit()
        if convergence_point == "no":
            fairy_follow = input("You turn around and go back into the woods, you see a beautiful little fairy, do you follow them? (yes/no): ").lower()  
            if fairy_follow == "yes":
                peek_inside = input("Okay! You follow them down a narrow path in the forest, and come across an ivy-covered cabin. The fairy went inside! Do you want to peek into the window?: ").lower()  # Convert input to lowercase
                if peek_inside == "yes":
                    print("You see other fairys; she has a whole fairy family!!")
                else:
                    print("Maybe that was a good decision, it could have been a trap!! You decide not to open the chest and continue your adventure.") 
                    print(f"Better to be safe than sorry, you never know with those fairys...You continue on your way, and find yourself lost in the woods, but you hear some footsteps...and someone whispering your name...{first_name.capitalize()}")
                    weapon = input("You should probably find something to protect yourself, just in case. What do you grab? (rock/stick): ").lower()
                    print("You hold your " +str(weapon) +" close and hope you don't run into some bad characters!")  
                    print("You tiptoe your way through and decide its probably best to not get into a scrap with these people you don't know")  
                    direction = input("You find yourself at a clearing with two different ways to go, which way do you choose? (left/right): ")
                    if direction in ("left", "right"):
                            convergence_point = input("You continue your journey and eventually arrive at a mysterious cave entrance. Do you enter? (yes/no): ").lower()
                    if convergence_point == "yes":
                        print("You enter the cave and discover a hidden treasure room.")
                        print("Congratulations! You've successfully completed your adventure and found a treasure!")
                        quit()
    else:
        print("You just got stuck and drowned! YOU HAVE DIED!")
        quit()
    print("You tiptoe your way through and decide its probably best to not get into a scrap with these people you don't know")    
    direction = input("You find yourself at a clearing with two different ways to go, which way do you choose? (left/right): ")
    if direction in ("left", "right"):
        convergence_point = input("You continue your journey and eventually arrive at a mysterious cave entrance. Do you enter? (yes/no): ").lower()
        if convergence_point == "yes":
                print("You enter the cave and discover a hidden treasure room.")
                print("Congratulations! You've successfully completed your adventure and found a treasure!")
                quit()
        if convergence_point == "no":
            fairy_follow = input("You turn around and go back into the woods, you see a beautiful little fairy, do you follow them?: ").lower()  
    if fairy_follow == "yes":
        peek_inside = input("You follow them down a narrow path in the forest, and come across an ivy-covered cabin that the fairy goes to hide in, do you peek in the window?: ").lower()  
        if peek_inside == "yes":
            print("You see other fairies; she has a whole fairy family!!") 
            print("You slowly step away so they don't hear you and become startled, we don't know what they are capable of...")
            print("As you continue through the woods, you stumble into the swamp, you find a hidden treasure chest!")
            treasure = input("Do you open the treasure chest? (yes/no): ").lower()
            convergence_point = input("You continue your journey and eventually arrive at a mysterious cave entrance. Do you enter? (yes/no): ").lower()
            if convergence_point == "yes":
                print("You enter the cave and discover a hidden treasure room.")
                print("Congratulations! You've successfully completed your adventure and found a treasure!")
                quit()
            else:
                print(f"You get chased by a panther, trip and fall. He has eaten you. YOU DIED! RIP {first_name.capitalize()}")
                quit()

    go_swamp = input("You find yourself back at the murky swamp...do you go around it to avoid getting stuck?: (yes/no): ")
    if go_swamp == "yes":
        print("Good decision!!") 
        fairy_follow = input("You see a beautiful little flying fairy, do you follow them? ").lower()  
        if fairy_follow == "yes":
            peek_inside = input("You follow them down a narrow path in the forest, and come across an ivy-covered cabin that the fairy goes to hide in, do you peek in the window?").lower()  
            if peek_inside == "yes":
                print("You see other fairies; she has a whole fairy family!!")
                print("You slowly step away so they don't hear you and become startled, we don't know what they are capable of...")
                print("As you continue through the woods, you stumble into the swamp, you find a hidden treasure chest!")
                treasure = input("Do you open the treasure chest? (yes/no): ").lower()
                convergence_point = input("You continue your journey and eventually arrive at a mysterious cave entrance. Do you enter? (yes/no): ").lower()
                if convergence_point == "yes":
                    print("You enter the cave and discover a hidden treasure room.")
                    print("Congratulations! You've successfully completed your adventure and found a treasure!")
                    quit()
                else:
                     print(f"You get chased by a panther, trip and fall. He has eaten you. YOU DIED! RIP {first_name.capitalize()}")
                     quit()
    else:
        print("You get the hell out of there, stumble into a clearing where you start to feel a little hazy")

    take_break = input("Do you stop to take a rest? (yes/no): ")
    if take_break == "yes":
        print("You find a nice spot in the clearing and lay down...zzz")        
        convergence_point = input("You wake up and continue your journey and eventually arrive at the mysterious cave entrance. Something is following you, you have no choice but to enter Do you enter? (yes/no): ").lower()
        if convergence_point == "yes":
                print("You enter the cave and discover a hidden treasure room.")
                print("Congratulations! You've successfully completed your adventure and found a treasure!")
                quit()
        else:
            print(f"It was a panther, and he rips you to shreds. YOU HAVE DIED! RIP to the brave {first_name.capitalize()}")
            exit()
    else:
        convergence_point = input("You continue your journey and eventually arrive back at the mysterious cave entrance. Something is following you, you have no choice but to enter, Do you enter? (yes/no): ").lower()
        if convergence_point == "yes":
                print("You enter the cave and discover a hidden treasure room.")
                print("Congratulations! You've successfully completed your adventure and found a treasure!")
                quit()
        else:
            print(f"It was a panther, and he rips you to shreds. YOU HAVE DIED! RIP {first_name.capitalize()}")
            exit()
        


elif direction == "right":
    fairy_follow = input("You see a beautiful little flying fairy, do you follow them?: ").lower()  
    if fairy_follow == "yes":
        peek_inside = input("You follow them down a narrow path in the forest, and come across an ivy-covered cabin that the fairy goes to hide in, do you peek in the window?: ").lower()  
        if peek_inside == "yes":
            print("You see other fairies; she has a whole fairy family!!")
            print("You slowly step away so they don't hear you and become startled, we don't know what they are capable of...")
            print("As you continue through the woods, you stumble into the swamp, you find a hidden treasure chest!")
            treasure = input("Do you open the treasure chest? (yes/no): ").lower()

            if treasure == "yes":
                 print("Congratulations! You've found a chest full of gold coins. You're rich!")
                



            else:
                 print("The risk just wasn't worth it, I don't blame you. Let's keep going...") 
                 print("You continue on your way, and find yourself lost in the woods, but you hear some footsteps...")
                 weapon = input("You should probably find something to protect yourself, just in case. What do you grab? (rock/stick): ").lower()
                 print("You hold your " +str(weapon) +" close and hope you don't run into some bad characters!")
                 convergence_point = input("You continue your journey and eventually arrive at a mysterious cave entrance. Do you enter? (yes/no): ").lower()
                 if convergence_point == "yes":
                    print("You enter the cave and discover a hidden treasure room.")
                    print("Congratulations! You've successfully completed your adventure and found a treasure!")
                    quit()
                 if convergence_point == "no":
                   fairy_follow = input("You turn around and go back into the woods, you see a beautiful little fairy, do you follow them? (yes/no): ").lower()  
                 if fairy_follow == "yes":
                    peek_inside = input("You follow them down a narrow path in the forest, and come across an ivy-covered cabin that the fairy goes to hide in, do you peek in the window?: ").lower()  # Convert input to lowercase
        if peek_inside == "yes":
            print("You see other fairies; she has a whole fairy family!!")
            go_swamp = input("You then continue on your way and run into a murky swamp...do you go around it to avoid getting stuck? (yes/no): ")
            if go_swamp == "yes":
                print("Good decision!!")
            else:
                print(f"You fall into the swamp, getting grabbed my a massive crocidile in the process, YOU DIED! RIP {first_name.capitalize()}")
                exit()
    else:            
        take_break = input("You start to feel a little sleepy...do you want to stop to take a rest? (yes/no): ")
        if take_break == "yes":
            print("You find a nice spot in the clearing and lay down...zzz")

        convergence_point = input(f"{first_name.upper()}!!!You wake up and continue your journey and eventually arrive at a mysterious cave entrance. Do you enter? (yes/no): ").lower()
        if convergence_point == "yes":
                print("You enter the cave and discover a hidden treasure room.")
                print("Congratulations! You've successfully completed your adventure and found a treasure!")
                quit()
        else:
            convergence_point = input("You find yourself in a circle, almost as if on purpose... are you lost?...You keep moving and you eventually arrive back at the mysterious cave entrance!! Creepy... Something is following you, you have no choice but to enter, Do you enter? (yes/no): ").lower()
            if convergence_point == "yes":
                print("You enter the cave and discover a hidden treasure room.")
                print("Congratulations! You've successfully completed your adventure and found a treasure!")
                quit()
            else:
                print(f"It was a panther, and he rips you to shreds. YOU HAVE DIED! Rest in Pieces, {first_name.capitalize()}")
                exit()




