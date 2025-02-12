import pygame
import random
import time

import pygame.display


class Cell:

    def __init__(self,coordinates,size=50,line_width=2, border_colour = (255,0,0)):
        
        self.x, self.y = coordinates
        
        self.walls = {"North": True,
                      "East":True,
                      "South":True,
                      "West":True
                      } 
        
        self.size = 50
        self.line_width = 2
        self.border_colour = self.border_colour

    def draw_cell(self):
        pass

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
        self.cell_walls = [[1,2,3,4]] * self.rows * self.columns
        
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

                pygame.draw.rect(self.window,self.border_colour,
                (current_x, starting_y,self.block_size,self.block_size),width=2)

                self.cells.append((current_x, starting_y))
                
                #show the grid being made
                #pygame.display.update()
                #time.sleep(0.5)
    
    def generate_maze(self):
        
        visited = []
        start_position = random.randint(0,len(self.cells))
        print(start_position)

        while len(visited) != len(self.cells):
            

            north = 1
            east = 1
            south = 1
            west = 1


    def available_walls(self,cell_number):
        return self.cell_walls[cell_number]
    
    def create_wall(self, start_coordinates, end_coordinates):

        pygame.draw.line(self.window,self.background_colour,start_coordinates, end_coordinates,width = 2)
        #pygame.display.update()

    def get_details(self):
        print(len(self.cells))

        #for cell in self.cells:
        #    print(cell)
        
        print(len(self.cell_walls))

        for cell in self.cell_walls:
            print(cell)


    def run(self):
        
        running = True
        while running:
            pygame.display.update()


mg = Mazegenerator(rows=5,columns=6)
mg.draw_grid()
#mg.get_details()
#mg.create_wall((40,100),(100,30))
mg.generate_maze()
mg.run()