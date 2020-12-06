#Grid
L = [ [6,0,5,4,7,0,0,1,3],
      [0,0,4,1,0,2,8,0,9],
      [0,1,9,5,0,0,0,7,6],
      [3,0,2,6,0,0,0,0,0],
      [1,0,7,2,5,4,3,6,0],
      [0,0,0,0,0,0,7,0,2],
      [0,0,0,3,4,5,1,8,0],
      [0,5,0,0,0,0,0,0,4],
      [0,7,0,0,0,5,0,2,5]
    ]



#Lists
lock = [ [False for i in range (9)] for j in range (9)]
solved = [ [False for i in range (9)] for j in range (9)]
solvedSudoku = [ [0 for i in range (9)] for j in range (9)]
NUMBERS = [str(x) for x in range(0,10)]

#Mesurements
WIDTH = 666
HEIGHT = 666
BOX_WIDTH = WIDTH//9
BOX_HEIGHT = HEIGHT//9

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0,255,0)
GREY = (161, 161, 161)
BLUE = (70, 182, 238)
RED = (232, 31, 71)


#Parameters
run = True
locked = False
