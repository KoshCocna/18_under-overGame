import random


rule = "Under and Over 7 is a very simple dice game. It is usually played with two wooden dice. " \
       "The principle of Under and Over 7 is to guess whether the value of the dice is lower\higher" \
       "than or equal to 7. These are the only bets in the game"

game_is_on = True
money = 100


def roll():
       dice1 = random.randint(1, 6)
       dice2 = random.randint(1, 6)
       res = dice1 + dice2
       print(f"It's {res}")
       if res > 7:
              return 'o'
       elif res < 7:
              return 'u'
       else:
              return '7'

while game_is_on:
       wager = int(input("Pls enter your wager: "))
       if wager > money:
              print("You don't have enough money.")
              continue

       choice = input(
              "Pls make your choice! \nIf under 7, then enter 'u'.\nIf over 7, then enter 'o'.\nIf 7, then enter 7: ")

       if roll() == choice:
              money += wager
              print(f"You win this bet!\nYour current money is {money}")
       else:
              money -= wager
              print(f"You lost this bet...\nYour current money is {money}")
       if 'q' == input("If you want to quit, then press Q!") or money < 0:
              game_is_on = False
