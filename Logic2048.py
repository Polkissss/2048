import random

class logic:

    # Function supposed to create an empty plane with only one added value
    def CreatePlane(PLANE):
        for i in range(4):
            PLANE.append([0]*4)
        logic.TileChoosing(PLANE)
        return PLANE

    # Function to check if there are any empty places if are adds one value (2 or 4) to randomly chosen one, else return True to end game loop as player has lost
    def TileChoosing(PLANE):
        # Making list with indexes of empty tiles on a PLANE
        empty = []
        for i in range(4):
            for j in range(4):
                if PLANE[i][j] == 0:
                    empty.append([i, j])
        # Check if there are any empty tiles to add new values into if NO player lost and returns True 
        if len(empty) == 0:
            return True
        # If there is any empty tile add randomly choosen 2 or 4 to it and return False
        else:
            chosenSlot = random.choice(empty)
            PLANE[chosenSlot[0]][chosenSlot[1]] = random.choice([2,4])
            return PLANE
    
    # Move to the left
    def Left(PLANE):
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
        return PLANE
    
    # Move to the right
    def Right(PLANE):
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
        return PLANE
    
    # Move down
    def Down(PLANE):
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
        return PLANE
    
    # Move up
    def Up(PLANE):    
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
        return PLANE
    
    # Checking if theres a winning value on a plane
    def WinningCondition(PLANE, limit):
        for i in range(4):
            for j in range(4):
                if PLANE[i][j] == limit:
                    return True
        return False