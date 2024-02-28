import getpass
print("Let's play rock, paper, scissor")

player1_lives = 3
player2_lives = 3
player_alive = True


while player_alive:
    player1 = getpass.getpass(prompt=f"\33[32mPlayer 1\33[0m you have {player1_lives} lives left, please pick your next move:\nR for Rock\nS for Scissor\nP for Paper\n",stream=None)
    player2 = getpass.getpass(prompt=f"\33[34mPlayer 2\33[0m you have {player2_lives} lives left, please pick your next move:\nR for Rock\nS for Scissor\nP for Paper\n", stream=None)

    if len(player1) != 1 or player1.lower() not in ["r", "s", "p"]:
        print("Invalid Input Player 1\n")
    elif len(player2) != 1 or player2.lower() not in ["r", "s", "p"]:
        print("Invalid Input Player 2\n")
    else:
        if player1.lower() == "r" and player2.lower() == "s":
            player2_lives -= 1
            print("\33[32mPlayer 1\33[0m won \33[34mPlayer 2\33[0m loses a life")
        elif player1.lower() == "s" and player2.lower() == "p":
            player2_lives -= 1
            print("\33[32mPlayer 1\33[0m won \33[34mPlayer 2\33[0m loses a life")
        elif player1.lower() == "p" and player2.lower() == "r":
            player2_lives -= 1
            print("\33[32mPlayer 1\33[0m won \33[34mPlayer 2\33[0m loses a life")
        elif player2.lower() == "r" and player1.lower() == "s":
            player1_lives -= 1
            print("\33[34mPlayer 2\33[0m won \33[32mPlayer 1\33[0m loses a life")
        elif player2.lower() == "s" and player1.lower() == "p":
            player1_lives -= 1
            print("\33[34mPlayer 2\33[0m won \33[32mPlayer 1\33[0m loses a life")
        elif player2.lower() == "p" and player1.lower() == "r":
            player1_lives -= 1
            print("\33[34mPlayer 2\33[0m won \33[32mPlayer 1\33[0m loses a life")
        elif player1.lower() == player2.lower():
            print("Tie\n")

        if player1_lives == 0:
            print("\33[32mPlayer 1\33[0m lost")
            player_alive = False
        elif player2_lives == 0:
            print("\33[34mPlayer 2\33[0m lost")
            player_alive = False
        else:
            print("\nTime for the next round\n")
