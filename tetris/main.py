import sys

from settings import *

# components
from Game import Game
from Preview import Preview
from Score import Score



class Main:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        # components
        self.game = Game()
        self.preview = Preview()
        self.score = Score()



    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill(BG_COLOR)

            # components
            self.game.run()
            self.preview.run()
            self.score.run()

            pg.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    main = Main()
    main.run()
