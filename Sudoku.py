import numpy as np
import pygame
from Settings import *
pygame.init()
pygame.font.init()

#Solver functions
def check(y, x, o):
    global L
    for i in range(9):
        if L[y][i] == o:
            return False

    for i in range(9):
        if L[i][x] == o:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range (3):
            if L[y0+i][x0+j] == o:
                return False
    return True

def solve(window):
    for col in range(9):
        for row in range(9):
            if (L[col][row] == 0):
                for num in range(1,10):
                    if check(col,row,num):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                                
                        L[col][row] = num
                        solved[col][row] = True
                        
                        drawGame(window)
                        pygame.time.delay(50)
                        solve(window)
                        if (checkSolved()):
                            return
                        pygame.draw.rect(window, RED, (row*BOX_WIDTH, col*BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT))
                        pygame.display.update()
                        pygame.time.delay(50)
                        drawGame(window)
                        
                        solved[col][row] = False
                        L[col][row] = 0
                return


#Pygame functions
def drawGrid(window):
    for i in range(1,10):
        if (i%3 != 0):
            pygame.draw.line(window, BLACK, (i*WIDTH/9 , 0) , (i*WIDTH/9 , HEIGHT) , 2)
        else:
            pygame.draw.line(window, BLACK, (i*WIDTH/9 , 0) , (i*WIDTH/9 , HEIGHT) , 5)

    for i in range(1,10):
        if (i%3 != 0):    
            pygame.draw.line(window, BLACK, (0 , i*HEIGHT/9) , (WIDTH, i*HEIGHT/9) , 2)
        else:
            pygame.draw.line(window, BLACK, (0 , i*HEIGHT/9) , (WIDTH, i*HEIGHT/9) , 5)

def select(x,y):
    x = x//BOX_WIDTH
    y = y//BOX_HEIGHT
    selected[0] = x
    selected[1] = y

def drawSelection(window, select):
    if (select[0] != -1 or select[1] != -1):
        pygame.draw.rect(window, BLUE, (select[0]*BOX_WIDTH, select[1]*BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT), 5)

def drawNumbers(window):
    font = pygame.font.SysFont('Times New Roman', BOX_WIDTH//2)
    for col in range(9):
        for row in range(9):
            if (L[col][row] != 0):
                surface = font.render(str(L[col][row]), False, BLACK)
                window.blit(surface, (row*BOX_WIDTH + ((BOX_WIDTH - surface.get_width())//2), col*BOX_HEIGHT + ((BOX_HEIGHT - surface.get_height())//2)))

def lockGrid():
    for col in range(9):
        for row in range(9):
            if L[col][row] != 0:
                lock[col][row] = True
                solved[col][row] = True

def drawLocked(window):
    for col in range(9):
        for row in range(9):
            if (lock[col][row]):
                pygame.draw.rect(window, GREY, (row*BOX_WIDTH, col*BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT))

def checkSolved():
    for col in range(9):
        for row in range(9):
            if (not solved[col][row]):
                return False
    return True

def drawSolved(window):
    for col in range(9):
        for row in range(9):
            if (solved[col][row] and not lock[col][row]):
                pygame.draw.rect(window, GREEN, (row*BOX_WIDTH, col*BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT))                
    
def drawGame(window):
    win.fill(WHITE)
    drawLocked(window)
    drawSolved(window)
    drawGrid(window)
    drawNumbers(window)
    drawSelection(window, selected)
    pygame.display.update()

#Game
win = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Sudoku")

selected = [-1,-1]
while run:
    drawGame(win)
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickedX, clickedY = pygame.mouse.get_pos()
            select(clickedX, clickedY)

        if event.type == pygame.KEYDOWN:
            if (event.unicode in NUMBERS):
                if(selected != [-1, -1] and lock[selected[1]][selected[0]] == False):
                    L[selected[1]][selected[0]] = int(event.unicode)
                    
            elif (event.unicode == ""):
                selected = [-1, -1]
            elif (event.unicode == "l" or event.unicode == "L"):
                lockGrid()
                locked = True
            elif (event.unicode == "s" or event.unicode == "S"):
                if (locked):
                    selected = [-1, -1]
                    solve(win)
            elif (event.unicode == "r" or event.unicode == "R"):
                L = [ [0 for i in range(9)] for j in range(9)]
                lock = [ [False for i in range (9)] for j in range (9)]
                solved = [ [False for i in range (9)] for j in range (9)]
                solvedSudoku = [ [0 for i in range (9)] for j in range (9)]
                drawGame(win)
                
                

pygame.font.quit()
pygame.quit()
quit()
