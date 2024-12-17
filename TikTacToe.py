import pygame


class TikTakToe:

    def __init__(self):
        pygame.init()

        background_colour = (197, 145, 149)
        self.width, self.height = (300, 300)

        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(background_colour)
        pygame.display.set_caption("Tik Tak Toe")

    def draw_grid(self):

        grid_width, grid_height = 300, 300

        line_start_locations = [(grid_width * 0.33, grid_height * 0.1), (grid_width * 0.66, grid_height * 0.1),
                                (grid_width * 0.1, grid_height * 0.33), (grid_width * 0.1, grid_height * 0.66)]
        line_end_locations = [(grid_width * 0.33, grid_height * 0.9), (grid_width * 0.66, grid_height * 0.9),
                              (grid_width * 0.9, grid_height * 0.33), (grid_width * 0.9, grid_height * 0.66)]

        for i, start_location in enumerate(line_start_locations):
            pygame.draw.line(self.window, (0, 0, 0), start_location, line_end_locations[i])

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                pygame.display.update()


TTT = TikTakToe()
TTT.draw_grid()
TTT.run()
