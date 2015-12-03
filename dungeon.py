# Dungeon game for Python practice
import random

# Requirements:
# - 

CELLS = [(0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)]

def get_locations():
  # monster = random location
  # door = random location
  # start = random location

  # if monster, door or start are the same run the process again

  # return monster, door, start


while True:
  print("Welome, welcome to dungeon!")
  print("You're currently in room {}")  # fill in with player position
  print("You can move {}")  # fill in with available moves
  print("Enter 'LET ME OUT' to get out")

  move = input("> ")
  move = move.upper()
  if move == "LET ME OUT":
    break

  # if it's a good move, change the player's position
  # if it's a bad move, don't change anything
  # if the new player position is the door, they win
  # if the new player position is the monster, they lose
  # otherwise continue...