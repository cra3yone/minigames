import pygame
import pygame.draw
import numpy as np
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
        
        self.game_grid = np.empty((3,3))

        self.cross_number = 1
        self.circle_number = 2

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

                self.cell_locations.append(cell_locations)

    def get_cell_clicked(self):
        
        current_x, current_y = pygame.mouse.get_pos()
        
        #print(f"{current_x = }, {current_y}")

        for i,cell in enumerate(self.cell_locations):
            if current_x > cell[0][0] and current_x < cell[3][0]:
                if current_y > cell[0][1] and current_y < cell[3][1]:
                    if self.cell_empty[i] != 1:
                        #print(f"Clicked on cell {i}")
                        #self.cell_locations.remove(cell)
                        self.cell_empty[i] = 1
                        #print(f"{self.cell_empty = }")
                        return i,cell
            
        return None,None
    
    def draw_cross(self,location):
        
        colour = (255,255,255)
        
        l1_start_x = location[0][0] * 1.1
        l1_start_y = location[0][1] * 1.1

        l1_end_x = location[3][0] * 0.9 
        l1_end_y = location[3][1] * 0.9

        l2_start_x = location[1][0] * 0.9
        l2_start_y = location[1][1] * 1.1

        l2_end_x = location[2][0] * 1.1
        l2_end_y = location[2][1] * 0.9

        pygame.draw.line(self.window, color=colour, start_pos=(l1_start_x, l1_start_y), end_pos=(l1_end_x,l1_end_y),width=3)
        pygame.draw.line(self.window, color=colour, start_pos=(l2_start_x, l2_start_y), end_pos=(l2_end_x,l2_end_y),width=3)

    def draw_circle(self,location):
        
        colour = (255,255,255)
        #print(location)
        center_x = (location[1][0] - location[0][0])/2 + location[0][0]
        center_y = (location[3][1] - location[0][1])/2 + location[0][1]

        #print(f"{center_x = }, {center_y = }")
        pygame.draw.circle(self.window, color=colour, center=(center_x,center_y),radius=25,width=4)

    def round_down(self, number):

        number = str(number)
        return int(number.split(".")[0])

    def update_game_board(self,ind, symbol):
        
        if symbol is None:
            return None

        #print(f"{ind = }")
        x = ind % 3
        y = self.round_down(ind/3)

        self.game_grid[y][x] = symbol
        #print(f"Places at {x = }, {y = }")
        #print(self.game_grid)

    def check_for_winner(self):
        
        cross_win = [self.cross_number] * 3
        circle_win = [self.circle_number] * 3

        cross_win = np.array(cross_win)
        circle_win = np.array(circle_win)

        for i in range(3):

            if (self.game_grid[i] == cross_win).all():
                print("cross won")
                return True
            
            if (self.game_grid[i] == circle_win).all():
                print("Circle won")
                return True

            if (self.game_grid[:, i] == cross_win).all():
                print("cross won")
                return True

            if (self.game_grid[:, i] == circle_win).all():
                print("Circle Won")
                return True

        if (self.game_grid.diagonal() == cross_win).all():
            print("Cross Won")
            return True
        
        if (self.game_grid.diagonal() == circle_win).all():
            print("Circle Won")
            return True
        
        return False


    def run(self):
        
        mouse_down = False
        x_turn = True
        running = True
        number_of_turns = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True

                if event.type == pygame.MOUSEBUTTONUP and mouse_down == True:
                    mouse_down = False
                    clicked_index,clicked_cell = self.get_cell_clicked()

                    if clicked_cell is not None:
                        number_of_turns += 1
                        if x_turn:
                            self.draw_cross(clicked_cell)
                            self.update_game_board(clicked_index, self.cross_number)
                            x_turn = False
                        else:
                            self.draw_circle(clicked_cell)
                            self.update_game_board(clicked_index, self.circle_number)
                            x_turn = True
                        
                        if self.check_for_winner():
                            running = False

                        if number_of_turns == 9:
                            print("It's a draw")
                pygame.display.update()


TTT = TikTakToe()
TTT.draw_grid((10,10),200)
TTT.run()
