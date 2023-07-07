import pygame
import Logic2048

# Constant variables such as colors, fps or size
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DISPLAYSIZE = (800, 600)
BLOCKSSIZE = (90, 90)
BUTTONSSIZE = (729, 70)
FPS = 60
GAMELIMIT = 2048 # Value to end the game (Default: 2048)

# Initializing pygame, creating a display and customizing it
pygame.init()
display = pygame.display.set_mode(DISPLAYSIZE)
pygame.display.set_caption("2048")
display.fill(WHITE)
pygame.display.update()

# Creating clock object to control framerate
clock = pygame.time.Clock()

# Fonts
TEXTFONT = pygame.font.Font("ASSETS/FONTS/Font.otf", 80)
menu2048Text = TEXTFONT.render("2048", True, BLACK)
menu2048Text = pygame.transform.smoothscale(menu2048Text, (350, 150))

# Number tiles
image0 = pygame.image.load("ASSETS/IMAGES/0.jpg").convert_alpha()
image0 = pygame.transform.smoothscale(image0, BLOCKSSIZE)
image2 = pygame.image.load("ASSETS/IMAGES/2.jpg").convert_alpha()
image2 = pygame.transform.smoothscale(image2, BLOCKSSIZE)
image4 = pygame.image.load("ASSETS/IMAGES/4.jpg").convert_alpha()
image4 = pygame.transform.smoothscale(image4, BLOCKSSIZE)
image8 = pygame.image.load("ASSETS/IMAGES/8.jpg").convert_alpha()
image8 = pygame.transform.smoothscale(image8, BLOCKSSIZE)
image16 = pygame.image.load("ASSETS/IMAGES/16.jpg").convert_alpha()
image16= pygame.transform.smoothscale(image16, BLOCKSSIZE)
image32 = pygame.image.load("ASSETS/IMAGES/32.jpg").convert_alpha()
image32 = pygame.transform.smoothscale(image32, BLOCKSSIZE)
image64 = pygame.image.load("ASSETS/IMAGES/64.jpg").convert_alpha()
image64 = pygame.transform.smoothscale(image64, BLOCKSSIZE)
image128 = pygame.image.load("ASSETS/IMAGES/128.jpg").convert_alpha()
image128 = pygame.transform.smoothscale(image128, BLOCKSSIZE)
image256 = pygame.image.load("ASSETS/IMAGES/256.jpg").convert_alpha()
image256 = pygame.transform.smoothscale(image256, BLOCKSSIZE)
image512 = pygame.image.load("ASSETS/IMAGES/512.jpg").convert_alpha()
image512 = pygame.transform.smoothscale(image512, BLOCKSSIZE)
image1024 = pygame.image.load("ASSETS/IMAGES/1024.jpg").convert_alpha()
image1024 = pygame.transform.smoothscale(image1024, BLOCKSSIZE)
image2048 = pygame.image.load("ASSETS/IMAGES/2048.jpg").convert_alpha()
image2048 = pygame.transform.smoothscale(image2048, BLOCKSSIZE)

# Button images
 
# Play
playButtonU = pygame.image.load("ASSETS/IMAGES/PLAYUNCLICKED.jpg").convert_alpha()
playButtonU = pygame.transform.smoothscale(playButtonU, BUTTONSSIZE)
playButtonC = pygame.image.load("ASSETS/IMAGES/PLAYCLICKED.jpg").convert_alpha()
playButtonC = pygame.transform.smoothscale(playButtonC, BUTTONSSIZE)
playRectangle = playButtonU.get_rect(topleft = (40, 280))
# Quit
quitButtonU = pygame.image.load("ASSETS/IMAGES/QUITUNCLICKED.jpg").convert_alpha()
quitButtonU = pygame.transform.smoothscale(quitButtonU, BUTTONSSIZE)
quitButtonC = pygame.image.load("ASSETS/IMAGES/QUITCLICKED.jpg").convert_alpha()
quitButtonC = pygame.transform.smoothscale(quitButtonC, BUTTONSSIZE)
quitRectangle = quitButtonU.get_rect(topleft = (40, 350))
# Settings
# playButtonU = pygame.image.load("ASSETS/IMAGES/PLAYUNCLICKED.jpg")
# playButtonU = pygame.transform.smoothscale(playButtonU, (729, 70))
# playButtonC = pygame.image.load("ASSETS/IMAGES/PLAYCLICKED.jpg")
# playButtonC = pygame.transform.smoothscale(playButtonC, (700, 200))

# Windows as well as their rectangles

# Losing and winning windows
youWonWindow = pygame.image.load("ASSETS/IMAGES/YOUWINWINDOW.jpg").convert_alpha()
youWonRectangle = youWonWindow.get_rect(center = (400, 300))
youLoseWindow = pygame.image.load("ASSETS/IMAGES/YOULOSEWINDOW.jpg").convert_alpha()
youLoseRectangle = youLoseWindow.get_rect(center = (400, 300))

# Ingame control window
controlsWindow = pygame.image.load("ASSETS/IMAGES/CONTROLS.jpg").convert_alpha()
controlsRectangle = controlsWindow.get_rect(topleft = (320, 0))

# Rectangle of poin400, 300t
point1 = pygame.Rect(20, 30, 20, 20)
point2 = pygame.Rect(120, 30, 20, 20)
point3 = pygame.Rect(220, 30, 20, 20)
point4 = pygame.Rect(320, 30, 20, 20)
point5 = pygame.Rect(20, 130, 20, 20)
point6 = pygame.Rect(120, 130, 20, 20)
point7 = pygame.Rect(220, 130, 20, 20)
point8 = pygame.Rect(320, 130, 20, 20)
point9 = pygame.Rect(20, 230, 20, 20)
point10 = pygame.Rect(120, 230, 20, 20)
point11 = pygame.Rect(220, 230, 20, 20)
point12 = pygame.Rect(320, 230, 20, 20)
point13 = pygame.Rect(20, 330, 20, 20)
point14 = pygame.Rect(120, 330, 20, 20)
point15 = pygame.Rect(220, 330, 20, 20)
point16 = pygame.Rect(320, 330, 20, 20)

# Important valuables that are constantly changing
playerWon = False
mouseReleased = False
mouseHolding = False
playHolding = False
quitHolding = False
mousePosition = (0, 0)

# Gameloop
def PlayingGame():

    # Creating ready plane to play
    PLANE = []
    PLANE = Logic2048.logic.CreatePlane(PLANE)
    PLANE = Logic2048.logic.TileChoosing(PLANE)

    while True:

        # Loop getting all events happening
        for event in pygame.event.get():
        # If event is closing window just quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # If player presses "z" key he goes to menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    return
            # If player releases one of the "move keys" the move is made and one new value is added
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    PLANE = Logic2048.logic.Left(PLANE)
                    PLANE = Logic2048.logic.TileChoosing(PLANE)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    PLANE = Logic2048.logic.Up(PLANE)
                    PLANE = Logic2048.logic.TileChoosing(PLANE)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    PLANE = Logic2048.logic.Right(PLANE)
                    PLANE = Logic2048.logic.TileChoosing(PLANE)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    PLANE = Logic2048.logic.Down(PLANE)
                    PLANE = Logic2048.logic.TileChoosing(PLANE)

        # If function supposed to return plane with new value returned True, if statement is triggered and the gameloop is stopping
        if PLANE == True:
            while True:
                # Waiting for player to either close window or press "z" key to go back to menu
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_z:
                            return
                        
                # Drawing you lose window  
                pygame.draw.rect(display, WHITE, (140, 210, 525, 180))
                display.blit(youLoseWindow, youLoseRectangle)
                pygame.display.update()

        #Filling display to hide last round
        display.fill(WHITE)

        # Displaying surfaces
        display.blit(menu2048Text, (435, 15))
        display.blit(controlsWindow, controlsRectangle)
        display.blit(globals().get("image" + str(PLANE[0][0])), point1.center)
        display.blit(globals().get("image" + str(PLANE[0][1])), point2.center)
        display.blit(globals().get("image" + str(PLANE[0][2])), point3.center)
        display.blit(globals().get("image" + str(PLANE[0][3])), point4.center)
        display.blit(globals().get("image" + str(PLANE[1][0])), point5.center)
        display.blit(globals().get("image" + str(PLANE[1][1])), point6.center)
        display.blit(globals().get("image" + str(PLANE[1][2])), point7.center)
        display.blit(globals().get("image" + str(PLANE[1][3])), point8.center)
        display.blit(globals().get("image" + str(PLANE[2][0])), point9.center)
        display.blit(globals().get("image" + str(PLANE[2][1])), point10.center)
        display.blit(globals().get("image" + str(PLANE[2][2])), point11.center)
        display.blit(globals().get("image" + str(PLANE[2][3])), point12.center)
        display.blit(globals().get("image" + str(PLANE[3][0])), point13.center)
        display.blit(globals().get("image" + str(PLANE[3][1])), point14.center)
        display.blit(globals().get("image" + str(PLANE[3][2])), point15.center)
        display.blit(globals().get("image" + str(PLANE[3][3])), point16.center)
        
        #Updating display
        pygame.display.update()

        # Using function to check win condition
        playerWon = Logic2048.logic.WinningCondition(PLANE, GAMELIMIT)

        # If win condition is true player won and gameloop is stopped
        if playerWon:
            while True:
                # Waiting for player to either close window or press "z" key to go back to menu
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_z:
                            return
                
                # Drawing you win window
                pygame.draw.rect(display, WHITE, (140, 210, 525, 180))
                display.blit(youWonWindow, youWonRectangle)
                pygame.display.update()

        #Setting framerate ceiling
        clock.tick(FPS)



# Main Menu loop
while True:
    # Loop getting all events happening
    for event in pygame.event.get():
        # If event is closing window just quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Check if player is moving mouse and return mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePosition = event.pos
        # Check if player released left mouse button 
        if event.type == pygame.MOUSEBUTTONUP:
            mouseReleased = True
        # Check if player is holding left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseHolding = True
        else:
            mouseHolding = False

    # Clearing display before adding any new surfaces to display
    display.fill(WHITE)

    # Displaying title in menu
    display.blit(menu2048Text, (220, 120))

    # Displaying play button pressed or unpressed version depending on whether player is holding mouse button on it or not
    if playHolding == False:
        display.blit(playButtonU, playRectangle)
    else:
        display.blit(playButtonC, playRectangle)

    # Displaying quit button pressed or unpressed version depending on whether player is holding mouse button on it or not
    if quitHolding == False:
        display.blit(quitButtonU, quitRectangle)
    else:
        display.blit(quitButtonC, quitRectangle)

    # Check if player is holding play button
    if playRectangle.collidepoint(mousePosition) and mouseHolding == True:
        playHolding = True
    # Check if player released play button and the game will start
    if playRectangle.collidepoint(mousePosition) and mouseReleased == True:
        mouseReleased = False
        playHolding = False
        PlayingGame()

    # Check if player is holding quit button
    if quitRectangle.collidepoint(mousePosition) and mouseHolding == True:
        quitHolding = True
    # Check if player released quit button resulting in quiting the game
    if quitRectangle.collidepoint(mousePosition) and mouseReleased == True:
        mouseReleased = False
        quitHolding = False
        pygame.quit()
        quit()

    # Updating display
    pygame.display.update()
    
    #Setting framerate ceiling
    clock.tick(FPS)

