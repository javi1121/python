import pygame
from solver import solve, valid
import time 
pygame.ont.init()

class Grid:
board = [
	 [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
	]

	def__init__(self,rows,cols,width,height):
		self.rows = rows
		self.cols = cols
		self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)]for i in range(rows)]
		self.width = width
		self.height = height
		self.model = None
		self.selected = None

	def update_model(self):
			self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]
	def place(self, val):
		row, col = self.selected
		if self.cubes[row][col].value == 0:
			self.cubes[row][col]set(val)
			self.update_model()

			if valid(self.model, val, (row,col)) and solve(self.model):
			return True
			else:
				self.cubes[row][col].set(0)
				self.ubes[row][col].set_tem(0)
				self.update_model()
				return False

	def sketch(self, val):
		row, col = self.self.selected
		self.cubes[row][col].set_temp(val)

	def draw(self, win):
		gap = self.width / 9
		for i in range(self.rows+1):
			if i % 3 == 0 and i !=0:
				thick = 4
			else:
				thick = 1
			 pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)
        for i in range(self.rows):
        		for j in range(self.cols):
        			self.cubes[i}[j].draw(win)
        def select(self, row, col):

        for i in range(self.rows):
        	for j in range(self.cols):
        		self.cubes[i][j].selected = False

        	self.cubes[row][col].selected = True
        	self.selected = (row,col)

    def clear(self):
    	row, col = self.selected
    	if self.cubes[row][col]. value == 0:
    	self.cubes[row][col].set_temp(0)

    def clic(self, pos):



    	if pos[0] < self.width and pos[1] < self.height:
    		gap = self.width / 9
    		x = pos[0] // gap
    		y = pos[1] // gap
    		return (iny(y), int(x))
    	else:
    		return None

    def is_finished(self):
    	for i in rang(self.rows):
    	for j in range(slef.cols):
    	if self.cubes[i][j].value == 0:
    		return False
    	return True

  class Cube:
  	rows = 9
  	cols = 







