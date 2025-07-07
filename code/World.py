import pygame
from code.Const import TILE_SIZE


class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            img_original = pygame.image.load(image_path).convert_alpha()
            original_width, original_height = img_original.get_size()
            aspect_ratio = original_height / original_width
            new_height = int(TILE_SIZE * aspect_ratio)
            self.image = pygame.transform.scale(img_original, (TILE_SIZE, new_height))
        except pygame.error:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE));
            self.image.fill((100, 100, 100))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = self.rect.inflate(-8, -8)


class Platform(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            img_original = pygame.image.load(image_path).convert_alpha()
            new_width = TILE_SIZE * 2
            original_width, original_height = img_original.get_size()
            aspect_ratio = original_height / original_width
            new_height = int(new_width * aspect_ratio)
            self.image = pygame.transform.scale(img_original, (new_width, new_height))
        except pygame.error:
            self.image = pygame.Surface((TILE_SIZE * 2, TILE_SIZE // 2));
            self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.move_counter = 0
        self.move_direction = 1
        self.speed = 1

    def update(self):
        self.rect.x += self.move_direction * self.speed
        self.move_counter += 1
        if self.move_counter > 80:
            self.move_direction *= -1
            self.move_counter = 0


class Portal(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            img_original = pygame.image.load(image_path).convert_alpha()
            new_width = int(TILE_SIZE * 1.5)
            original_width, original_height = img_original.get_size()
            aspect_ratio = original_height / original_width
            new_height = int(new_width * aspect_ratio)
            self.image = pygame.transform.scale(img_original, (new_width, new_height))
        except pygame.error:
            new_width = int(TILE_SIZE * 1.5)
            new_height = int(TILE_SIZE * 2.5)
            self.image = pygame.Surface((new_width, new_height));
            self.image.fill((100, 50, 0))

        self.rect = self.image.get_rect(bottomleft=(x, y))
