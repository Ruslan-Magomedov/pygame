from settings import *



class Preview:
    def __init__(self):
        self.surface = pg.Surface((SB_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION - PADDING))
        self.display_surface = pg.display.get_surface()



    def run(self):
        self.display_surface.blit(self.surface, (GAME_WIDTH + PADDING * 2, PADDING))