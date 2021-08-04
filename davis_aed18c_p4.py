# ==============================================================================
# PROGRAM: Rok, Paper, Scissors
#
# AUTHOR: Allyson Davis
# FSU MAIL NAME: aed18c
# RECITATION SECTION NUMBER: 8
# RECITATION INSTRUCTOR NAME: Kevin Yee
# CGS 3465 - Spring 2021
# PROJECT NUMBER: 4
# DUE DATE: 3/10/2021
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# This program will simulate the game rock, paper, scissors. Each player starts
# with $100 and pays the other player $10 each time they lose. The program will
# prompt the user for their choice and then a function will randomly choose
# for player 2.  The game is played repeatedly until either (1) one player has
# no money left or (2) the game has been played 20 times.
#
# INPUT
#
# This program asks the user for the choice of 1, 2 or 3, indicating Rock, Paper
# or Scissors. Error checking will be done and keep prompting the user until
# they enter a valid choice.
#
# OUTPUT
#
# After each play of the game, print out the following in clear format: the
# choices each player made (print both the number giving the choice, and the
# word which describes it), which player won the game (or indicate a tie), and
# the amount of money each player has left. At the end of the program run print
# out a summary giving the total number of games actually played, the total
# number of games each player won, the number of tied games, the percentage of
# games won by each player, and the identity of the overall winner.
#
# ASSUMPTIONS
#
# We assume that the user enters a number when asked for a number.
#
# ==============================================================================

import random

# ==============================================================================
# GLOABL NAMED CONSTANTS
# choices 1, 2, 3
ROCK = 1
PAPER = 2
SCISSORS = 3

#max games played
MAX_GAMES = 20
# ==============================================================================
# MAIN FUNCTION
def main():
    p1GamesWon = 0
    p2GamesWon = 0
    gamesTied = 0
    totalGames = 0
    p1Bank = 100
    p2Bank = 100
    winner = 0
    overallWinner = 0

    PrintHeader()
    
    while (totalGames < MAX_GAMES):
        p1Bank, p2Bank, winner = PlayOneMatch(p1Bank, p2Bank, winner)
        if (winner == 1):
            p1GamesWon = p1GamesWon + 1
        elif(winner == 2):
            p2GamesWon = p2GamesWon + 1
        else:
            gamesTied = gamesTied + 1
            
        totalGames = totalGames + 1

        if(p1Bank <= 0 or p2Bank <= 0):
            break

    if (p1GamesWon > p2GamesWon):
        overallWinner = 1
    elif(p2GamesWon > p1GamesWon):
        overallWinner = 2
    else :
        overallWinner = 0
        
    PrintFinalResults(p1GamesWon, p2GamesWon, gamesTied, totalGames, overallWinner) 
# ==============================================================================
def PrintHeader():
    # prints the output heading info for the user
    # called by main

    print("----------=====******=====----------")
    print("     Rock, Paper, and Scissors")
    print("----------=====******=====----------\n")

    print(" This program plays the EXCITING game of Rock, Paper, and Scissors.  Two players choose either Rock, Paper or Scissors, and the results of their picks are compared.  Each match is determined as follows:")
    print("\n\tPlayer 1\tPlayer 2\tResult")
    print("\t--------\t--------\t------")
    print("\tRock\t\tPaper\t\tPaper covers Rock.\tPlayer 2 wins!")
    print("\tPaper\t\tScissors\tScissors cuts Paper.\tPlayer 2 wins!")
    print("\tScissors\tRock\t\tRock breaks Scissors.\tPlayer 2 wins!")
    print("\t---\t\t---\t\tAny matching combo.\tA tie!")

    print("\n Now you are about to play a against world-class computer champion Dr. Windows.  You are Player 1, and the computer is Player 2.  Player 2's moves are randomly chosen by the computer. Both players start with $100 and the game is finished when either one player reaches $0 or there have been 3 matches played. The bet per match is $10.\n")

# ==============================================================================
def PrintFinalResults(p1Games, p2Games, tiedGames, gamesPlayed, winner):
    p1Percent = "{:.1%}".format(p1Games / gamesPlayed)
    p2Percent = "{:.1%}".format(p2Games / gamesPlayed)
    print("\n\n\n----------=====******=====----------\n")
    print("And there you have it, folks, the final matchoff between our two")
    print("contestants.  The final results for tonight's game are as follows:\n")
    print("\t\t\tPlayer 1   Player 2")
    print("\t\t\t========   ========")
    print(f'\tGames Won:\t{p1Games}\t\t{p2Games}')
    print(f'\tPercent Won:\t{p1Percent}\t\t{p2Percent}\n')
    print(f'\tTotal games tied:  {tiedGames}\n')
    print(f'\tTotal games played:  {gamesPlayed}\n')
    if(winner == 1):
        print("\tThe overall winnner is Player 1!\n")
    elif (winner == 2):
        print("\tThe overall winnner is Player 2!\n")
    else :
        print("\tThe overall game was tied!\n")
    print("Stop in again soon to play another exciting match!!!\n")    
    print("----------=====******=====----------\n")
# ==============================================================================
def PlayOneMatch(p1Bank, p2Bank, winner):
    p1Choice = GetPlayerChoice()
    p2Choice = DrawNum()

    winner = GetWinner(p1Choice, p2Choice)
    
    if(winner == 1):
        p1Bank = p1Bank + 10
        p2Bank = p2Bank - 10
    elif (winner == 2):
        p2Bank = p2Bank + 10
        p1Bank = p1Bank - 10

    p1Action = GetAction(p1Choice)
    p2Action = GetAction(p2Choice)

    PrintMove(p1Choice, p1Action, p2Choice, p2Action, winner, p1Bank, p2Bank)

    return (p1Bank, p2Bank, winner)
# ==============================================================================
def PrintMove(p1Choice, p1Action, p2Choice, p2Action, winner, p1Bank, p2Bank):
    spacer = "     "
    if (winner == 1):
        txtWinner = "Player 1"
    elif (winner == 2):
        txtWinner = "Player 2"
    else:
        txtWinner = "Tie"
    print("\n\nRESULTS OF THIS MOVE")
    print("=-=-=-=-=-=-=-=-=-=-")
    print("     Player 1            Player 2                   Player 1's   Player 2's")
    print(" Number    Action    Number    Action     Winner       Money       Money")
    print(" ------    ------    ------    ------     ------       -----       -----")
    print(f'{spacer}{p1Choice}{spacer}{p1Action}{spacer}   {p2Choice}{spacer}  {p2Action}{spacer}{txtWinner}!{spacer}    {p1Bank}{spacer}{spacer}{p2Bank}')
# ==============================================================================
def GetPlayerChoice():
    player_choice = int(input("\nPlayer 1, Enter your choice of\n\t1 Rock\n\t2 Paper\n\t3 Scissors -> "))
    # if player does NOT enter 1, 2, or 3: prompt user again
    while (player_choice != ROCK and player_choice != PAPER and player_choice != SCISSORS):
        player_choice = int(input("\nInvalid option. Enter your choice of\n\t1 Rock\n\t2 Paper\n\t3 Scissors -> "))

    return player_choice
# ==============================================================================
def DrawNum():
    return random.randint(ROCK,SCISSORS)
# ==============================================================================
def GetWinner(one, two):
    # determines and reutrns winner
    if (one == ROCK):
        if(two == ROCK):
            winner = 0
        elif(two == PAPER):
            winner = 2
        elif(two == SCISSORS):
            winner = 1
    elif (one == PAPER):
        if(two == ROCK):
            winner = 1
        elif(two == PAPER):
            winner = 0
        elif(two == SCISSORS):
            winner = 2
    elif (one == SCISSORS):
        if(two == ROCK):
            winner = 2
        elif(two == PAPER):
            winner = 1
        elif(two == SCISSORS):
            winner = 0            
    return winner

# ==============================================================================
def GetAction(num):
    if (num == ROCK):
        return "Rock"
    elif (num == PAPER):
        return "Paper"
    elif (num == SCISSORS):
        return "Scissors" 
# ==============================================================================
main()
# ==============================================================================
#                                 END OF PROGRAM
# ==============================================================================
