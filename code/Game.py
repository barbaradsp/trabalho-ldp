import pygame
from code.Const import *
from code.Menu import Menu
from code.Level import Level
from code.WinScreen import WinScreen


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.game_state = 'menu'

    def run(self):
        while True:
            if self.game_state == 'menu':
                menu = Menu(self.window)
                menu_return = menu.run()
                if menu_return == 'INICIAR':
                    self.game_state = 'level'
                elif menu_return == 'SAIR':
                    break

            elif self.game_state == 'level':
                level = Level(self.window, 'level1')
                level_return = level.run()
                if level_return == 'win':
                    self.game_state = 'win'
                else:
                    self.game_state = 'menu'

            elif self.game_state == 'win':
                win_screen = WinScreen(self.window)
                win_screen.run()
                self.game_state = 'menu'

        pygame.quit()
        quit()
