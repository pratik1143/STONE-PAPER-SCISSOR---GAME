import random , sys
from turtledemo.nim import randommove


print("***** WELCOME TO THE GAME  ******")
print("LOADING***********************************************")
win = 0
lose = 0
tie = 0
while True:
    print('%s win ,%s lose ,%s tie' % (win,lose,tie))
    while True:
        player_choice= input("Enter your move: rock(R), paper(P),scisor(s),quit(q)")
        player_choice = player_choice.upper()
        if player_choice == 'q' or player_choice == 'Q':
            print('-'*40)
            sys.exit()
        if player_choice == 'P' or player_choice == 'R' or player_choice == 'S':
            break
        print("enter any P,R,S,Q")

    if player_choice == 'R':
        print("ROCK VERSUS")
    elif player_choice == 'P':
        print("PAPER VERSUS")
    elif player_choice == 'S':
        print("scissor  versus")

    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        computerMove = 'R'
        print("ROCK")
    elif randomnumber == 2:
        computerMove = 'S'
        print("SCISSOR")
    elif randomnumber == 3:
        computerMove = 'P'
        print("PAPER")

    if player_choice == computerMove:
        print("its a tie")
        tie += 1
    elif player_choice == 'P' and computerMove == 'S':
        print("you win")
        win += 1
    elif player_choice == 'S' and computerMove == 'P':
        print("you lose")
        lose += 1
    elif player_choice == 'R' and computerMove == 'S':
        print("you win")
        win += 1
    elif player_choice == 'S' and computerMove == 'R':
        print("you lose")
        lose += 1
    elif player_choice == 'S' and computerMove == 'P':
        print("you win")
        win += 1
    elif player_choice == 'P' and computerMove == 'S':
        print("you lose")
        lose += 1
