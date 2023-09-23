player1 =input("Enter a choice (rock, paper, scissors): ")
player2 =input("Enter a choice (rock, paper, scissors): ")

if player1 == player2:
    print("Player1 and Player2 selected the same choice so It's a draw!!")
elif player1 == "rock":
    if player2 == "paper":
        print("Paper covers rock. Paper win!")
#    else:
#        print("Scissors cuts paper. You lose.")
elif player1 == "rock":
    if player2 == "scissors":
        print("Rock smashes scissors. Rock win!")
#    else:
#        print("Paper covers rock. You lose.")
elif player1 == "paper":
    if player2 == "scissors":
        print("Scissors cuts paper. Scissors win!")
#    else:
#        print("Rock smashes scissors. You lose.")