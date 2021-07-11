import pygame
from pygame import mixer
import time

#Initialization
pygame.init()
screen = pygame.display.set_mode((560,670))
running = True
background = pygame.image.load('.\\Images\\bg.jpeg')
wrong = pygame.image.load('.\\Images\\false.png')
font = pygame.font.Font('freesansbold.ttf', 38)
pygame.mixer.music.load('.\\Images\\bgaudio.wav')
pygame.mixer.music.play(-1)

grid = [[6, 0, 9, 0, 0, 4, 0, 0, 1], 
         [8, 0, 0, 0, 5, 0, 0, 0, 0], 
         [0, 3, 5, 1, 0, 9, 0, 0, 8], 
         [0, 0, 8, 0, 0, 0, 0, 0, 4], 
         [0, 5, 0, 0, 0, 0, 0, 3, 0], 
         [4, 0, 0, 0, 7, 0, 0, 5, 2], 
         [0, 0, 0, 0, 0, 1, 0, 0, 0], 
         [0, 0, 1, 0, 4, 0, 0, 0, 0], 
         [7, 6, 0, 9, 3, 0, 0, 0, 0]]

class Box():
    def __init__(self, row, col, val = None, default = 0):
        self.row = row
        self.col = col
        self.val = val
        self.temp = 0
        self.default = 0
        self.confirm = 0

class Board():
    def __init__(self,grid, row, col, width, height, gap, start_x, start_y, screen):
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.screen = screen
        self.gap = gap
        self.start_x = start_x
        self.start_y = start_y
        self.board = [[Box(rows,cols,grid[rows][cols],1)for cols in range(self.col)] for rows in range(self.row)] 
        self.selected = None
        self.wrong = 0
        self.play_time = 0

        for rows in range(self.row):
            for cols in range(self.col):
                if self.board[rows][cols].val != 0:
                    self.board[rows][cols].default = 1
    
    def printBoard(self):
        print('-'*37)
        for i, row in enumerate(self.board):
            print(("|" + " {}   {}   {} |"*3).format(*[x.val if x.val != 0 else " " for x in row]))
            if i == 8:
                print('-'*37)
            elif i % 3 == 2:
                print("|" + "---+"*8 + "---|")
            else:
                print("|" + "   +"*8 + "   |")

    def drawGrid(self):
        for rows in range(self.row + 1):
            if rows % 3 == 0 or rows == 0 or rows == 10:
                line_width = 3
            else:
                line_width = 1
            pygame.draw.line(self.screen, (0,0,0), (20, rows * self.gap + 20), (self.width + 20, rows * self.gap + 20), line_width)
            pygame.draw.line(self.screen, (0,0,0), (rows * self.gap + 20, 20), (rows * self.gap + 20, self.height + 20), line_width)

    def drawVal(self):
        for rows in range(self.row):
            for cols in range(self.col):
                word_x = cols * self.gap + 40
                word_y = rows * self.gap + 35

                if self.board[rows][cols].val != 0 or self.board[rows][cols].temp != 0:
                    if self.board[rows][cols].default == 1:
                        val_text = font.render(str(self.board[rows][cols].val), True, (0,0,0))
                        screen.blit(val_text, (word_x, word_y))

                    else: 
                        if self.board[rows][cols].confirm == 0:
                            medium_font = pygame.font.Font('freesansbold.ttf', 20)
                            val_text = medium_font.render(str(self.board[rows][cols].temp), True, (102, 51, 0))
                            screen.blit(val_text, (word_x - 10, word_y - 10))
                    
                        else:
                            val_text = font.render(str(self.board[rows][cols].val), True, (102,51,0))
                            screen.blit(val_text, (word_x, word_y))

    def selectData(self, x, y):
        if x < 20 or y < 20 or x > 560 or y > 560:
            self.selected = None
        else:
            selected_row = (y - 20)//self.gap
            selected_col = (x - 20)//self.gap
            self.selected = [selected_row, selected_col]
    
    def highlightBox(self):
        if self.selected != None:
            row = self.selected[0]
            col = self.selected[1]
            pygame.draw.rect(self.screen, (255,0,0), ((20 + col * self.gap, 20 + row * self.gap), (60, 60)), 3)
    
    def drawWrong(self):
        screen.blit(wrong,(self.selected[1]* 60 + 35, self.selected[0]* 60 + 35))
    
    def formatTime(self):
        minute = 0
        minute = self.play_time//60
        second = self.play_time - minute * 60
        time = f"{minute:02}:{second:02}"
        time_text = font.render(time, True, (0,0,0))
        screen.blit(time_text, (450, 600))

    def drawLogo(self):
        small_font = pygame.font.Font('freesansbold.ttf', 16)
        medium_font = pygame.font.Font('freesansbold.ttf', 22)
        val_text1 = small_font.render("Reset = Press C" , True, (51,25,0))
        val_text2 = small_font.render("Solve = Press Space", True, (51,25,0))
        val_text3 = small_font.render("Crack Sudoku", True, (0,0,0))
        screen.blit(val_text1, (20, 580))
        screen.blit(val_text2, (20, 600))
        screen.blit(val_text3, (20, 620))

    def inputTemp(self,key):
        if self.selected != None:
            row = self.selected[0]
            col = self.selected[1]
            if self.board[row][col].default == 0:
                self.board[row][col].temp = key
                self.board[row][col].val = 0
                self.board[row][col].confirm = 0

    def enterVal(self):
        if self.selected != None:
            row = self.selected[0]
            col = self.selected[1]
            if self.board[row][col].temp != 0:
                if (self.is_safe(row,col,self.board[row][col].temp)):
                    self.board[row][col].val = self.board[row][col].temp
                    self.board[row][col].temp = 0
                    self.board[row][col].confirm = 1
                else:
                    self.wrong = 1
                    self.board[row][col].temp = 0
    
    def delVal(self):
        if self.selected != None:
            row = self.selected[0]
            col = self.selected[1]
            if self.board[row][col].default == 0:
                self.board[row][col].val = 0
                self.board[row][col].temp = 0
                self.board[row][col].confirm = 0
    
    def clearVal(self):
        for rows in range(self.row):
            for cols in range(self.col):
                if self.board[rows][cols].default == 0:
                    self.board[rows][cols].val = 0
                    self.board[rows][cols].temp = 0

    def findboxRange(self, val):
        if val < 3:
            return 0, 3
        elif val>=3 and val < 6:
            return 3, 6
        else:
            return 6, 9
    
    def movetoNext(self, x, y):
        if y < 8:
            return x, y+1
        else:
            return x+1, 0

    def isSafe(self, curr_x, curr_y, val):
        if(curr_x > self.row or curr_y > self.col or curr_x < 0 or curr_y < 0 or self.board[curr_x][curr_y].val != 0):
            return False

        for i in range (self.row):
            if self.board[curr_x][i].val == val or self.board[i][curr_y].val == val:
                return False
        
        r1,r2 = self.find_boxRange(curr_x)
        c1,c2 = self.find_boxRange(curr_y)
        for r in range(r1,r2):
            for c in range(c1,c2):
                if self.board[r][c].val == val:
                    return False
        return True
    
    def findSol(self, curr_x, curr_y):
        self.print_board()
        if curr_x == 8 and curr_y == 9:
                return True

        if curr_y == 9:
            curr_x,curr_y = self.movetoNext(curr_x,curr_y)

        while self.board[curr_x][curr_y].val != 0:
            curr_x, curr_y = self.movetoNext(curr_x, curr_y)
        
        for possible_sol in range(1,10):
            if (self.is_safe(curr_x, curr_y, possible_sol)):
                self.board[curr_x][curr_y].val = possible_sol
                self.selected = [curr_x, curr_y]
                # self.update_win()

                if (self.findSol(curr_x, curr_y + 1)):
                    return True
                
                else:
                    self.board[curr_x][curr_y].val = 0
                    self.selected = [curr_x, curr_y]
                    # self.update_win()
        return False

    def solver(self):
        for rows in range(self.row):
            for cols in range(self.col):
                if self.board[rows][cols].default == 0:
                    self.board[rows][cols].val = 0
                    self.board[rows][cols].temp = 0
                    self.board[rows][cols].confirm = 1
        self.updateWin()
        self.selected = [0,0]
        self.find_sol(0,0)

    def updateWin(self):
        self.screen.blit(background,(0,0))
        self.drawGrid()
        self.drawVal()
        self.highlightBox()
        self.formatTime()
        self.drawLogo()
        if self.wrong == 1:
            self.drawWrong()
            self.wrong = 0
            pygame.display.update()
            pygame.time.delay(500)
        pygame.display.update()

sudoku = Board(grid, 9, 9, 540, 540, 60, 20, 20, screen)
start = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            sudoku.selectData(x,y)
        
        if event.type == pygame.KEYDOWN:
            if sudoku.selected != None:
                if event.key == pygame.K_LEFT:
                    sudoku.selected[1] = sudoku.selected[1] - 1 if sudoku.selected[1] > 0 else sudoku.selected[1]
                if event.key == pygame.K_RIGHT:
                    sudoku.selected[1] = sudoku.selected[1] + 1 if sudoku.selected[1] < sudoku.col-1 else sudoku.selected[1]
                if event.key == pygame.K_UP:
                    sudoku.selected[0] = sudoku.selected[0] - 1 if sudoku.selected[0] > 0 else sudoku.selected[0]
                if event.key == pygame.K_DOWN:
                    sudoku.selected[0] = sudoku.selected[0] + 1 if sudoku.selected[0] < sudoku.row - 1 else sudoku.selected[0]
                if event.key == pygame.K_1:
                    sudoku.inputTemp(1)
                if event.key == pygame.K_2:
                    sudoku.inputTemp(2)
                if event.key == pygame.K_3:
                    sudoku.inputTemp(3)
                if event.key == pygame.K_4:
                    sudoku.inputTemp(4)
                if event.key == pygame.K_5:
                    sudoku.inputTemp(5)
                if event.key == pygame.K_6:
                    sudoku.inputTemp(6)
                if event.key == pygame.K_7:
                    sudoku.inpuTemp(7)
                if event.key == pygame.K_8:
                    sudoku.inputTemp(8)
                if event.key == pygame.K_9:
                    sudoku.inputTemp(9)
                if event.key == pygame.K_RETURN:
                    sudoku.enterVal()
                if event.key == pygame.K_BACKSPACE:
                    sudoku.delVal()
                if event.key == pygame.K_SPACE:
                    sudoku.solver()
                if event.key == pygame.K_c:
                    sudoku.clearVal()


    playTime = round(time.time() - start)
    sudoku.playTime = playTime
    sudoku.updateWin()