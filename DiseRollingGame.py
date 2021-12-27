#A global variable for save winners list
winners = []


#findwinner function for find the winner)
def findwinner(scores=[],*args):

    #using max method to find out the winner and getting winner index
    winner = scores.index(max(scores))

    if winner == 0:
        print("\nThe winner is Player 1!")
    elif winner == 1:
        print("\nThe winner is Player 2!")
    elif winner == 2:
        print("\nThe Winner is Player 3!")
    elif winner == 3:
        print("\nThe winner is Player 4!")
        
    return winner+1

#reroll function for even numbers
def reroll():
    rerollQA = input("Do you want to re roll for higher score? (y/n)")
    return(bool(rerollQA == "y"))
        

#Play game function
def Play(n):

    
    #Players totals
    p1tot = p2tot = p3tot = p4tot = 0

    #Repeat game for 4 rounds
    for j in range(1,5):
        print("\n------------Round {}------------".format(j))

        #Player marks in one round
        for i in range(1,n+1):
            p = int(input("Rolling dice for player {} : ".format(i)))

            #Checking player number
            if i == 1:
                
                #Calculation part
                if p % 2 == 0:
                    p1tot += p
                    rerollQ = reroll()
                    
                    #Rerolling for evens
                    if rerollQ:
                        print("**Rolling dice again for player {} **".format(i))
                        r = int(input())
                        if r % 2 == 0:
                            p1tot += r
                        else:
                            p1tot -= r    
                else:
                    p1tot -= p

            #Checking player number    
            elif i == 2:

                #Calculation part
                if p % 2 == 0:
                    p2tot += p
                    rerollQ = reroll()

                    #rerolling for evens
                    if rerollQ:
                        print("**Rolling dice again for player {} **".format(i))
                        s = int(input())
                        if s % 2 == 0:
                            p2tot += s
                        else:
                            p2tot -= s    
                else:
                    p2tot -= p

            #Checking player number    
            elif i == 3:

                #Calculation part
                if p % 2 == 0:
                    p3tot += p
                    rerollQ = reroll()
                    
                    #Rerolling for evens
                    if rerollQ:
                        print("**Rolling dice again for player {} **".format(i))
                        t = int(input())
                        if t % 2 == 0:
                            p3tot += t
                        else:
                            p3tot -= t    
                else:
                    p3tot -= p
                    
            #Checking player number
            elif i == 4:
                
                #Calculation part
                if p % 2 == 0:
                    p4tot += p
                    rerollQ = reroll()
                    
                    #Rerolling for evens
                    if rerollQ:
                        print("**Rolling dice again for player {} **".format(i))
                        u = int(input())
                        if u % 2 == 0:
                            p4tot += u
                        else:
                            p4tot -= u   
                else:
                    p4tot -= p   
             #End of one round

        #End of 4 rounds

    played = [p1tot,p2tot,p3tot,p4tot]

    #Creating an array list of players scores
    players = played[0:n]

    #Calling findwinner function to find the winner
    winner = findwinner(players)

    #Return message for completing
    return winner
    

#Game function implementation
def Game():        
    #Welcome message
    print("+++++++++ Welcome to odd/even Dice Game +++++++++\n")

    #add rules here
    print("Rules of the game :\n")
    print("1. To play this game there should be more than one people and less than 5 people(1..4)")
    print("2. Each player has 4 rounds")
    print("3. Even numbers will added to player's total and odds will reduced from total")
    print("4. If a player got an even number, player can re roll dice for once(to go for a higher mark)")
    print("5. At the end of four rounds, the highest scorer will win.\n")

    #getting input of number of players
    nop = int(input("Enter the number of players: "))

    #checking the validity of number of players 
    if nop > 1 and nop < 5:
        #Calling play game function
        s = Play(nop)

        #End of a game
            
        #calling global varible winners for update list
        global winners
        winners.append(s)
        
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++")
        #asking on player about replay
        replay = input("\nDo you want to play again? (y/n)")

        #Checking player decision
        if replay == "y":
            Game()
        else:
            print("\n                Game Over!")

            #Display the list of winners
            Print("Winners List : \n")
            for j in winners:
                print(j)

            print("\n++++++++++++++++++++++++++++++++++++++++++++++++")


#Calling Game function for start the game            
p = Game()
