import random
from readchar import readkey, key
from os import system, name

# Creating function to clear terminal
def clear():
  if name == 'nt':
    system('cls')
  else:
    system('clear')

# Winning value of a game. Change to make a default value different. It has to be any power of a 2 starting from at least 2**3 (8).
limit = 2048

# Function containing options screen
def ChangeSettings():
    global limit
    clear()
    print("--------Settings----------")
    print("1. Value limit")
    print("2. Back to menu")
    print()
    w = input("Which option you want to choose?: ")
    
    match w:
      # Option 1 to change Value limit of the game (default: 2048)
      case "1":
        clear()
        print("1. 128")
        print("2. 256")
        print("3. 512")
        print("4. 1024")
        print("5. 2048")
        print("6. 4096")
        z = input("Choose: ")
        if z in ["1", "2", "3", "4", "5", "6"]:
          z = int(z)
          limit = 2**(6 + z)
          input("Your current limit is " + str(limit) + "! Press enter to go back to settings menu.")
        else:
          input("Bad input! Press enter to go back to settings menu.")
      # option 2 to go back to main menu
      case "2":
        return
      # Invalid input
      case _:
        clear()
        input("Bad input! Press enter to go back to options menu.")
    ChangeSettings()
  

# Function choosing one random empty tile and adding either 2 or 4 to it. Returns True if player lost, False if is still playing.
def TileChoosing():
  # Making list with indexes of empty tiles on a PLANE
  empty = []
  for i in range(4):
    for j in range(4):
      if PLANE[i][j] == 0:
        empty.append([i, j])
  # Check if there are any empty tiles to add new values into if NO player lost and returns True 
  if len(empty) == 0:
    print("You lost! No empty tiles on a PLANE. Press enter to go back to main menu.")
    input()
    return True
  # If there is any empty tile add randomly choosen 2 or 4 to it and return False
  else:
    chosenSlot = random.choice(empty)
    PLANE[chosenSlot[0]][chosenSlot[1]] = random.choice([2,4])
    return False

# Making a "move" to the left
def Left():
  for each in range(3):
    for i in range(4):
          for j in range(4)[::-1]:
            # Checking if current element is on the edge of PLANE. Necessary to not go out of list index
            if j != 0:
                # If the next value is the same as current. Add them and place on next position
                if PLANE[i][j] != 0 and PLANE[i][j-1] == PLANE[i][j]:
                      PLANE[i][j-1] = 2*PLANE[i][j]
                      PLANE[i][j] = 0
                # If next tile is empty push current value into it
                if PLANE[i][j] != 0 and PLANE[i][j-1] == 0:
                      PLANE[i][j-1] = PLANE[i][j]
                      PLANE[i][j] = 0

# Making a "move" to the right
def Right():
    for each in range(3):
      for i in range(4):
          for j in range(4):
            # Checking if current element is on the edge of PLANE. Necessary to not go out of list index
            if j != 3:
                # If the next value is the same as current. Add them and place on next position
                if PLANE[i][j] != 0 and PLANE[i][j+1] == PLANE[i][j]:
                      PLANE[i][j+1] = 2*PLANE[i][j]
                      PLANE[i][j] = 0
                # If next tile is empty push current value into it
                if PLANE[i][j] != 0 and PLANE[i][j+1] == 0:
                      PLANE[i][j+1] = PLANE[i][j]
                      PLANE[i][j] = 0

# Making a "move" down
def Down():
    for each in range(3):
      for j in range(4):
          for i in range(4):
            # Checking if current element is on the edge of PLANE. Necessary to not go out of list index
            if i != 3:
                # If the next value is the same as current. Add them and place on next position
                if PLANE[i][j] != 0 and PLANE[i+1][j] == PLANE[i][j]:
                      PLANE[i+1][j] = 2*PLANE[i][j]
                      PLANE[i][j] = 0
                # If next tile is empty push current value into it
                if PLANE[i][j] != 0 and PLANE[i+1][j] == 0:
                      PLANE[i+1][j] = PLANE[i][j]
                      PLANE[i][j] = 0

# Making a "move" up
def Up():    
    for each in range(3):
      for j in range(4):
        for i in range(4)[::-1]:
          # Checking if current element is on the edge of PLANE. Necessary to not go out of list index
          if i != 0:
              # If the next value is the same as current. Add them and place on next position
              if PLANE[i][j] != 0 and PLANE[i-1][j] == PLANE[i][j]:
                    PLANE[i-1][j] = 2*PLANE[i][j]
                    PLANE[i][j] = 0
              # If next tile is empty push current value into it
              if PLANE[i][j] != 0 and PLANE[i-1][j] == 0:
                    PLANE[i-1][j] = PLANE[i][j]
                    PLANE[i][j] = 0

# Defining main loop
def MainGameloop():

  # Adding new value (2 or 4) to random empty tile at the beginning of each turn. Check if player lost
  if TileChoosing():
    return
  
  # Printing PLANE and asking player to make a move
  for i in range(4):
    print(str(PLANE[i][0]), str(PLANE[i][1]), str(PLANE[i][2]), str(PLANE[i][3]), sep="|", end="|\n")
    print("-" * 30)
  print()
  print("Press a key (wasd or arrows) to make a move in a corresponding direction")
  print("Press a key \"z\" to quit and go back to menu")

  # contantly checking if player pressed a key and making a move
  while True:
    k = readkey()
    match k:
      case key.UP:
        clear()
        Up()
        break
      case key.DOWN:
        clear()
        Down()
        break
      case key.RIGHT:
        clear()
        Right()
        break
      case key.LEFT:
        clear()
        Left()
        break
      case "w":
        clear()
        Up()
        break
      case "s":
        clear()
        Down()
        break
      case "d":
        clear()
        Right()
        break
      case "a":
        clear()
        Left()
        break
      case "z":
        print()
        confirmation = input("Are you sure? (Yes/No): ").capitalize()
        if confirmation == "Yes" or confirmation == "Y":
          return
        else:
          continue

  # Checking if there is a value limit on a PLANE (default: 2048) in other words if player has won
  for i in range(4):
    for j in range(4):
      if PLANE[i][j] == limit:
        for i in range(4):
          print(str(PLANE[i][0]), str(PLANE[i][1]), str(PLANE[i][2]), str(PLANE[i][3]), sep="|", end="|\n")
          print("-" * 30)
        print("You won!1!1!!11!")
        input("Press enter to go back to main menu.")
        return
        
  MainGameloop()

while True:
  # Printing menu and its options
  clear()
  print("----------2048-------------")
  print("1. -PLay game-")
  print("2. -Settings-")
  print("3. -Wyjdź z gry-")
  print()
  choice = input("Choose option: ")
  
  match choice:
    # Option 1 create an empty PLANE and start a main gameloop
    case "1":
      PLANE = []
      for i in range(4):
        PLANE.append([0]*4)
      TileChoosing()
      clear()
      
      MainGameloop()
    # Option 2 change settings
    case "2":
      ChangeSettings()
    # Optiom 3 exit the game. Requires confirmation
    case "3":
      clear()
      potwierdzenie = input("Are you sure you want to quit? (Yes/No): ")
      potwierdzenie = potwierdzenie.capitalize()
      if potwierdzenie == "Yes" or potwierdzenie == "Y":
        exit()
    # Invalid option
    case _:
      clear()
      input("Invalid input! Press enter to go back to main menu.")