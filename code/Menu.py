import pygame
from code.Const import *

class Menu:
    def __init__(self, window):
        self.window = window
        try:
            self.surf = pygame.image.load('./asset/background.png').convert()
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        except pygame.error:
            self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            self.surf.fill((135, 206, 235))

        self.font = pygame.font.Font(None, 74)

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.window.blit(text_surface, text_rect)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Ove Melaa - Heaven Sings.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, (0, 0))

            for i, option in enumerate(MENU_OPTION):
                color = YELLOW if i == menu_option else WHITE
                self.draw_text(option, color, WIN_WIDTH / 2, 300 + i * 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            pygame.display.flip()