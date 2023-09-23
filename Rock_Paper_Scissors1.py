player1 = input(" Enter Your Choice (rock, paper, scissors:   )")
player2 = input(" Enter Your Choice (rock, paper, scissors:   )")

if player1 == player2:
    print("You both selected the same choice. So it`s a draw!!")
elif player1 == "rock":
    if player2 == "paper":
        print("Paper Wins!")
    #else:
        #print("Scissors Wins!")
elif player1 == "rock":
    if player2 == "scissors":
        print("rock win!")
    #else:
       # print("paper wins!")
elif player1 == "paper":
    if player2 == "scissors":
        print("Scissors wins!")
   # else:
      #  print("rock wins!")
