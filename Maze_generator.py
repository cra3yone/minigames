import pygame
import pygame.display 

class Mazegenerator:

    def __init__(self):
        
        pygame.init()

        self.height = 500
        self.width = 700
        self.background_colour = (0,255,0)

        window = pygame.display.set_mode((self.width,self.height))
        window.fill(self.background_colour)
    
    def run(self):
        
        running = True
        while running:
            pygame.display.update()


mg = Mazegenerator()
mg.run()