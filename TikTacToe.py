import pygame
import pygame.draw


class TikTakToe:

    def __init__(self):
        pygame.init()

        background_colour = (197, 145, 149)
        self.width, self.height = (300, 300)

        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(background_colour)
        pygame.display.set_caption("Tik Tak Toe")

    def draw_grid(self, start_position, size):


        for i in range(1,3):

            pygame.draw.line(self.window, (0,0,0), (start_position[0], size*0.33*i + start_position[1]),
                             (size+start_position[0], start_position[1] + size*0.33*i))
            
            pygame.draw.line(self.window,(0,0,0), (size*0.33*i + start_position[0], start_position[1]),
                             (start_position[0] + size *0.33*i, size+start_position[1]))

            #add a grid position for each "square" in the grid


    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                pygame.display.update()


TTT = TikTakToe()
TTT.draw_grid((10,10),200)
TTT.run()
