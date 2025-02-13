import pygame
import random
import time

import pygame.display
import pygame.draw


class Cell:

    def __init__(self,coordinates,size=50,line_width=2, border_colour = (255,0,0)):
        
        self.x, self.y = coordinates
        
        self.walls = {"North": True,
                      "East":True,
                      "South":True,
                      "West":True
                      } 
        
        self.size = size
        self.line_width = line_width
        self.border_colour = border_colour
        self.visited = False
    
    def draw_cell(self, window):
        self.window = window
        pygame.draw.rect(self.window,self.border_colour,(self.x, self.y,self.size,self.size),width = self.line_width)

    def remove_wall(self,direction):
        
        if direction == "North":
            starting_coordinate = (self.x,self.y)
            ending_coordinate = (self.x + self.size, self.y)

        elif direction == "East":
            starting_coordinate = (self.x, self.y)
            ending_coordinate = (self.x, self.y + self.size)

        elif direction == "South":
            starting_coordinate = (self.x, self.y+self.size)
            ending_coordinate = (self.x + self.size, self.y + self.size)

        else:
            starting_coordinate = (self.x + self.size, self.y)
            ending_coordinate = (self.x + self.size, self.y + self.size)

        pygame.draw.line(self.window,(157,146,245),starting_coordinate, ending_coordinate,width = self.line_width*2)

    def get_coordinates(self):
        return (self.x, self.y)
    
    def get_walls(self):
        return self.walls

    def get_size(self):
        return self.size

    def get_line_width(self):
        return self.line_width    

    
class Mazegenerator:

    def __init__(self,rows=5,columns=5):
        
        pygame.init()

        self.rows = rows
        self.columns = columns

        self.height = 500
        self.width = 700
        self.background_colour = (157,146,245)

        self.window = pygame.display.set_mode((self.width,self.height))
        self.window.fill(self.background_colour)

        self.cells = []
        #self.cell_walls = [[1,2,3,4]] * self.rows * self.columns
        
        self.block_size = 50

        self.start_location = (20,20)
        self.border_colour = (255,0,0)

    def draw_grid(self):

        starting_x, starting_y = self.start_location
        starting_y -= self.block_size

        for i in range(self.rows):

            starting_y += self.block_size

            for j in range(self.columns):

                current_x = starting_x + (j*self.block_size)

                new_cell = Cell((current_x,starting_y),size=self.block_size, line_width=1)

                new_cell.draw_cell(self.window)
                self.cells.append(new_cell)

                pygame.display.update()
                #time.sleep(0.5)
    
    def generate_maze(self):
        
        stack = []

        oc = 4

        self.cells[oc].border_colour = (0,255,0)
        self.cells[oc].draw_cell(self.window)
        print(self.available_walls(self.cells[oc]))
        
    def available_walls(self,current_cell):

        x,y = current_cell.get_coordinates()

        start_x, start_y = self.start_location

        x_limit = (self.columns - 1) * self.block_size + start_x
        y_limit = (self.rows - 1) * self.block_size + start_y


        print(f"{x_limit = }, {y_limit = }")
        print(f"{x = } ,{y = }")

        cell_walls = current_cell.walls
        wall_keys = list(cell_walls.keys())

        if y == start_y:
            #remove North
            cell_walls[wall_keys[0]] = False

        if x == x_limit:
            #remove East
            cell_walls[wall_keys[1]] = False

        if y == y_limit:
            #remove south
            cell_walls[wall_keys[2]] = False
            
        if x == start_x:
            #remove west
            cell_walls[wall_keys[3]] = False
            

        return cell_walls
    
    def create_wall(self, start_coordinates, end_coordinates):

        pygame.draw.line(self.window,self.background_colour,start_coordinates, end_coordinates,width = 2)
        #pygame.display.update()

    def run(self):
        
        running = True
        while running:
            pygame.display.update()


mg = Mazegenerator(rows=7,columns=5)
mg.draw_grid()
mg.generate_maze()
mg.run()