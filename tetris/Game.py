from settings import *



class Game:
    def __init__(self):
        self.surface = pg.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pg.display.get_surface()



    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pg.draw.line(self.surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1)

        for row in range(1, ROWS):
            x = row * CELL_SIZE
            pg.draw.line(self.surface, LINE_COLOR, (0, x), (self.surface.get_width(), x), 1)            



    def run(self):
        self.display_surface.blit(self.surface, ([PADDING] * 2))
        self.draw_grid()
