import pygame
from code.Const import *
from code.Player import Player
from code.World import Tile, Platform, Portal
from code.Enemy import Enemy


class Level:
    def __init__(self, window, level_name):
        self.window = window
        self.player = None
        level_map = [
            '           ',
            '           ',
            '           ',
            '      E   D',
            '     322224',
            '   5       ',
            '  5        ',
            '           ',
            '2          ',
            '12E        ',
            '1122224    ',
            '        5  ',
            '           ',
            '          2',
            '     5   21',
            'P  2LLL2211',
            '  211111111',
            '22111111111',
        ]

        self.tiles = pygame.sprite.Group()
        self.moving_platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.lava = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()
        for row_index, row in enumerate(level_map):
            for col_index, tile_char in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                try:
                    tile_num = int(tile_char)
                    if tile_num in TILE_LEGEND:
                        tile = Tile(TILE_LEGEND[tile_num], x, y)
                        self.tiles.add(tile)
                except ValueError:
                    if tile_char == 'M':
                        platform = Platform('./asset/castleHalf.png', x, y)
                        self.moving_platforms.add(platform)
                    elif tile_char == 'E':
                        enemy = Enemy('slimeWalk', x, y)
                        self.enemies.add(enemy)
                    elif tile_char == 'L':
                        lava_tile = Tile('./asset/liquidLavaTop_mid.png', x, y)
                        self.lava.add(lava_tile)
                    elif tile_char == 'D':
                        y_for_bottom = (row_index + 1) * TILE_SIZE
                        self.portal = Portal('./asset/portal.png', x, y_for_bottom)
                        self.portal_group.add(self.portal)
                    elif tile_char == 'P':
                        self.player = Player(x, y)
        try:
            self.background_img = pygame.image.load('./asset/background.png').convert()
            self.background_img = pygame.transform.scale(self.background_img, (WIN_WIDTH, WIN_HEIGHT))
        except pygame.error:
            self.background_img = pygame.Surface((WIN_WIDTH, WIN_HEIGHT));
            self.background_img.fill((135, 206, 235))

    def run(self):
        clock = pygame.time.Clock()
        game_font = pygame.font.Font(None, 80)  # Fonte para a mensagem de morte

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            game_status = self.player.update(self.tiles.sprites(), self.moving_platforms.sprites(), self.enemies,
                                             self.lava)

            self.enemies.update(self.tiles.sprites(), self.moving_platforms.sprites())
            self.moving_platforms.update()

            self.window.blit(self.background_img, (0, 0))
            self.tiles.draw(self.window)
            self.moving_platforms.draw(self.window)
            self.enemies.draw(self.window)
            self.lava.draw(self.window)
            self.portal_group.draw(self.window)
            self.window.blit(self.player.image, self.player.rect)

            if hasattr(self, 'portal') and self.player.rect.colliderect(self.portal.rect):
                return 'win'

            if game_status == 'game_over':
                text_surf = game_font.render("Você morreu!", True, YELLOW).convert_alpha()
                text_rect = text_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

                self.window.blit(text_surf, text_rect)
                pygame.display.flip()

                pygame.time.wait(1000)
                return 'game_over'

            pygame.display.flip()
