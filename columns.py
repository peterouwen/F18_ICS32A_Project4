import pygame
import sys
from faller import Faller

blockColor = [(235, 60, 39), (236, 219, 83), (0, 162, 138), (173, 94, 153), (150, 79, 76), (148, 170, 211),
              (247, 205, 204), (136, 176, 75), (95, 75, 139), (255, 111, 97)]
gameBoard = []
bottomLine = [12, 12, 12, 12, 12, 12]
faller = Faller()

def initBoard():
    for i in range(12):
        temp = []
        for j in range(6):
            temp.append(-1)
        gameBoard.append(temp)

def checkKeydownEvents(event, screen):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        faller.moveRight = True
        updateAct(screen)
    elif event.key == pygame.K_LEFT:
        faller.moveLeft = True
        updateAct(screen)
    elif event.key == pygame.K_SPACE:
        faller.rollBlock = True
        updateAct(screen)

def checkKeyupEvents(event):
    if event.key == pygame.K_RIGHT:
        faller.moveRight = False
    elif event.key == pygame.K_LEFT:
        faller.moveLeft = False
    elif event.key == pygame.K_SPACE:
        faller.rollBlock = False

def checkEvents(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, screen)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event)

def printBoard(screen):
    screen.fill((230, 230, 230))
    x_cood = 50
    y_cood = 50
    size = 50
    thickness = 3
    sideColor = (0, 0, 0)

    for i in range(12):
        for j in range(6):
            if gameBoard[i][j] == -1:
                pygame.draw.rect(screen, sideColor, [x_cood, y_cood, size, size], thickness)
            else:
                bgColor = blockColor[gameBoard[i][j]]
                pygame.draw.rect(screen, bgColor, [x_cood, y_cood, size, size])
            x_cood += size
        y_cood += size
        x_cood = 50

def checkLanded():
    if faller.bottomPos+1 == bottomLine[faller.pos]:
        bottomLine[faller.pos] -= 3
        return True
    else:
        return False

def updateAct(screen):
    global gameBoard
    #board = gameBoard.copy()
    if faller.moveRight:
        if faller.pos+1 <= 5 and bottomLine[faller.pos+1] > faller.bottomPos:
            if faller.bottomPos - 2 >= 0:
                gameBoard[faller.bottomPos-2][faller.pos+1] = gameBoard[faller.bottomPos-2][faller.pos]
            if faller.bottomPos - 1 >= 0:
                gameBoard[faller.bottomPos-1][faller.pos+1] = gameBoard[faller.bottomPos-1][faller.pos]
            gameBoard[faller.bottomPos][faller.pos+1] = gameBoard[faller.bottomPos][faller.pos]
            if faller.bottomPos - 2 >= 0:
                gameBoard[faller.bottomPos-2][faller.pos] = -1
            if faller.bottomPos - 1 >= 0:
                gameBoard[faller.bottomPos-1][faller.pos] = -1
            gameBoard[faller.bottomPos][faller.pos] = -1
            faller.pos += 1
            #gameBoard = board.copy()
            printBoard(screen)
            pygame.display.flip()
    if faller.moveLeft:
        if faller.pos-1 >= 0 and bottomLine[faller.pos-1] > faller.bottomPos:
            if faller.bottomPos - 2 >= 0:
                gameBoard[faller.bottomPos-2][faller.pos-1] = gameBoard[faller.bottomPos-2][faller.pos]
            if faller.bottomPos - 1 >= 0:
                gameBoard[faller.bottomPos-1][faller.pos-1] = gameBoard[faller.bottomPos-1][faller.pos]
            gameBoard[faller.bottomPos][faller.pos-1] = gameBoard[faller.bottomPos][faller.pos]
            if faller.bottomPos - 2 >= 0:
                gameBoard[faller.bottomPos-2][faller.pos] = -1
            if faller.bottomPos - 1 >= 0:
                gameBoard[faller.bottomPos-1][faller.pos] = -1
            gameBoard[faller.bottomPos][faller.pos] = -1
            faller.pos -= 1
            #gameBoard = board.copy()
            printBoard(screen)
            pygame.display.flip()
    if faller.rollBlock:
        faller.bottomBlock = (faller.bottomBlock+1) % 3
        if faller.bottomPos-2 >=0:
            gameBoard[faller.bottomPos-2][faller.pos] = faller.blocks[faller.bottomBlock]
        if faller.bottomPos-1 >= 0:
            gameBoard[faller.bottomPos-1][faller.pos] = faller.blocks[(faller.bottomBlock+1) % 3]
        gameBoard[faller.bottomPos][faller.pos] = faller.blocks[(faller.bottomBlock+2) % 3]
        printBoard(screen)
        pygame.display.flip()

def updateBoard(screen):
    if bottomLine.count(0) == 6:
        return (False, True)

    landFlag = False
    faller.bottomPos += 1
    print(faller.bottomPos)
    if faller.bottomPos == 0:
        while gameBoard[0][faller.pos] != -1:
            faller.pos = (faller.pos+1) % 6
        gameBoard[faller.bottomPos][faller.pos] = faller.blocks[faller.bottomBlock]
        print(gameBoard)
    elif faller.bottomPos == 1:
        gameBoard[faller.bottomPos][faller.pos] = faller.blocks[faller.bottomBlock]
        gameBoard[faller.bottomPos-1][faller.pos] = faller.blocks[(faller.bottomBlock+1) % 3]
        print(gameBoard)
    elif faller.bottomPos == 2:
        gameBoard[faller.bottomPos][faller.pos] = faller.blocks[faller.bottomBlock]
        gameBoard[faller.bottomPos-1][faller.pos] = faller.blocks[(faller.bottomBlock+1) % 3]
        gameBoard[faller.bottomPos-2][faller.pos] = faller.blocks[(faller.bottomBlock+2) % 3]
        print(gameBoard)
        if checkLanded():
            landFlag = True
            print(bottomLine)
    else:
        gameBoard[faller.bottomPos][faller.pos] = gameBoard[faller.bottomPos-1][faller.pos]
        gameBoard[faller.bottomPos-1][faller.pos] = gameBoard[faller.bottomPos-2][faller.pos]
        gameBoard[faller.bottomPos-2][faller.pos] = gameBoard[faller.bottomPos-3][faller.pos]
        gameBoard[faller.bottomPos-3][faller.pos] = -1
        print(gameBoard)
        if checkLanded():
            landFlag = True
            print(bottomLine)

    printBoard(screen)
    return (landFlag, False)

def runGame():
    pygame.init()
    screen = pygame.display.set_mode((400, 700))

    bg_color = (230, 230, 230)
    screen.fill(bg_color)
    x_cood = 50
    y_cood = 50
    size = 50
    thickness = 3
    sideColor = (0, 0, 0)
    clock = pygame.time.Clock()

    global faller
    initBoard()

    for i in range(12):
        for j in range(6):
            pygame.draw.rect(screen, sideColor, [x_cood, y_cood, size, size], thickness)
            x_cood += size
        y_cood += size
        x_cood = 50

    clock.tick(30)
    count = 0
    while True:
        checkEvents(screen)
        count += 1
        if count % 60 == 0:
            newFlag, endGame = updateBoard(screen)
            if endGame:
                sys.exit()
            if newFlag:
                faller = Faller()
        pygame.display.flip()

if __name__ == "__main__":
    runGame()