# Dungeon game for Python practice

import random

CELLS = [(0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)]

def get_locations():
  monster = random.choice(CELLS)
  door = random.choice(CELLS)
  start = random.choice(CELLS)

  # if monster, door or start are the same run the process again
  if monster == door or door == start:
    return get_locations()

  return monster, door, start

def move_player(player, move):
  # get the player position
  player_x, player_y = player

  if move == 'UP':
    player_x -= 1
  elif move == 'DOWN':
    player_x += 1
  elif move == 'LEFT':
    player_y -= 1
  elif move == 'RIGHT':
    player_y += 1
  
  return = player_x, player_y

def get_moves(player):
  moves =['LEFT', 'RIGHT', 'UP', 'DOWN']
  # player = (x, y)
  if player[0] == 0:
    moves.remove('UP')
  elif player[0] == 2:
    moves.remove('DOWN')

  if player[1] == 0:
    moves.remove('LEFT')
  elif player[1] == 2:
    moves.remove('RIGHT')

  return moves

def draw_map(player):
  print(" _ _ _ ")
  tile = "|{}"
  for idx, cell in enumerate(CELLS):
    if idx in (0, 1, 3, 4, 6, 7):
      if cell == player:
        print(tile.format('X'), end="")
      else:
        print(tile.format('_'), end="")
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))

monster, door, player = get_locations()
print("Welome, welcome to dungeon!")

while True:
  moves = get_moves(player)

  print("You're currently in room {}.".format(player))

  draw_map(player)

  print("You can move {}".format(moves))  # fill in with available moves
  print("Enter 'BEAM ME UP' to be teleported out")

  move = input("> ")
  move = move.upper()
  
  if move == "BEAM ME UP":
    break

  if move in moves:
    player = move_player(player, move)
  else:
    print("Walls are hard, stop walking into them")
    continue

  if player == door:
    print("You've escaped!")
    break
  elif player == monster:
    print("You've been gobbled up for breakfast!!")
    break

  # if it's a good move, change the player's position
  # if it's a bad move, don't change anything
  # if the new player position is the door, they win
  # if the new player position is the monster, they lose
  # otherwise continue...