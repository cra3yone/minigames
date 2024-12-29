import pygame
import pygame.draw
import time

import pygame.mouse

class TikTakToe:

    def __init__(self):
        pygame.init()

        background_colour = (197, 145, 149)
        self.width, self.height = (300, 300)

        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(background_colour)
        pygame.display.set_caption("Tik Tak Toe")

        self.start_position = None

        self.grid_size = None


        self.crosses_turn = False

        self.cell_locations = []
        self.cell_empty = [i*0 for i in range(9)]
        
        print(f"{self.cell_empty = }")

    def draw_grid(self, start_position, size):
        
        self.start_position = start_position
        self.grid_size = size

        for i in range(1,3):

            pygame.draw.line(self.window, (0,0,0), (start_position[0], size*0.33*i + start_position[1]),
                             (size+start_position[0], start_position[1] + size*0.33*i))
            
            pygame.draw.line(self.window,(0,0,0), (size*0.33*i + start_position[0], start_position[1]),
                             (start_position[0] + size *0.33*i, size+start_position[1]))

            #add a grid position for each "square" in the grid
        self.get_cell_locations()

    def get_cell_locations(self):
        
        start_x, start_y = self.start_position

        cell_size = self.grid_size * 0.33

        for i in range(3):
            current_y = start_y + cell_size*i
            for j in range(3):
                current_x = cell_size*j + start_x
                cell_locations = []
                cell_locations.append([current_x,current_y])
                cell_locations.append([current_x + cell_size, current_y])
                cell_locations.append([current_x, current_y + cell_size])
                cell_locations.append([current_x + cell_size, current_y + cell_size])

                print(f"{cell_locations =}")

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #print(f"{pygame.mouse.get_pos() = }")
                pygame.display.update()


TTT = TikTakToe()
TTT.draw_grid((0,0),200)
TTT.run()
