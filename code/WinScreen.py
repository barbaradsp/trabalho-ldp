import pygame
from code.Const import *


class WinScreen:
    def __init__(self, window):
        self.window = window
        try:
            self.background = pygame.image.load('./asset/background.png').convert()
            self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))
        except pygame.error:
            self.background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            self.background.fill((20, 40, 80))

        tamanho_fonte_grande = int(WIN_WIDTH / 6)
        tamanho_fonte_pequena = int(WIN_WIDTH / 14)

        self.font_grande = pygame.font.Font(None, tamanho_fonte_grande)
        self.font_pequena = pygame.font.Font(None, tamanho_fonte_pequena)

    def _draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color).convert_alpha()
        text_rect = text_surface.get_rect(center=(x, y))
        self.window.blit(text_surface, text_rect)

    def run(self):
        try:
            pygame.mixer_music.load('./asset/victory.mp3')
            pygame.mixer_music.play()
        except pygame.error:
            print("Arquivo de música de vitória não encontrado.")

        while True:
            self.window.blit(self.background, (0, 0))

            self._draw_text("Você ganhou!!", self.font_grande, YELLOW, WIN_WIDTH / 2, WIN_HEIGHT / 3)
            self._draw_text("Pressione ENTER para voltar ao menu", self.font_pequena, WHITE, WIN_WIDTH / 2,
                            WIN_HEIGHT / 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        pygame.mixer_music.stop()
                        return

            pygame.display.flip()
