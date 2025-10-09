import random
import sys

# Make use of this function whenever a player rolls a die
def roll_die() -> int:
    """Simulate a roll of a 6-sided die."""

    return random.randint(1, 6)

snakesAndLadders = {}


def game_setup(s, e):
    '''this is the setup of the game'''
    snakesAndLadders[s] = e


def player_turn(player : str, plyrSquare : int) -> int:
    diceRoll = roll_die()
    while diceRoll == 6:
        plyrSquare += diceRoll
        diceRoll = roll_die()
    plyrSquare += diceRoll

    return plyrSquare


def snake_or_ladder(plyr : str, plyrSquare : int) -> None:
    if plyrSquare in snakesAndLadders:
        newPlyrSquare = snakesAndLadders[plyrSquare]
        if newPlyrSquare > plyrSquare:
            print(f"Darn! A snake brought {plyr} down to square {newPlyrSquare}.")
        else:
            print(f"Splendid! {plyr} climbed a ladder up to square {newPlyrSquare}.")



def game_loop():
    for line in sys.stdin:
        
        if " " in line:
            s, e = line.split()
            game_setup(s, e)
        