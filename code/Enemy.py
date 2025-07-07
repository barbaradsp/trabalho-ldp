import pygame
from code.Const import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path_prefix, x, y):
        super().__init__()

        self.walk_frames = []
        self.frame_index = 0
        self.animation_counter = 0
        self.animation_cooldown = 15
        for i in range(1, 3):
            try:
                img_original = pygame.image.load(f'./asset/{image_path_prefix}{i}.png').convert_alpha()
                new_width = int(TILE_SIZE * 0.9)
                original_width, original_height = img_original.get_size()
                aspect_ratio = original_height / original_width
                new_height = int(new_width * aspect_ratio)
                img_scaled = pygame.transform.scale(img_original, (new_width, new_height))
                self.walk_frames.append(img_scaled)
            except pygame.error:
                img = pygame.Surface((30, 30));
                img.fill((255, 255, 0))
                self.walk_frames.append(img)

        self.image = self.walk_frames[self.frame_index]
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.hitbox = self.rect.inflate(-10, -10)

        self.move_direction = 1
        self.move_counter = 0
        self.speed = 1

        self.vel_y = 0

    def update(self, world_tiles, moving_platforms):
        dx = self.move_direction * self.speed
        dy = 0

        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        all_platforms = world_tiles + list(moving_platforms)
        for tile in all_platforms:
            if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y >= 0:
                    dy = tile.rect.top - self.rect.bottom
                    self.vel_y = 0

        self.move_counter += 1
        if self.move_counter > 80:
            self.move_direction *= -1
            self.move_counter = 0

        self.rect.x += dx
        self.rect.y += dy
        self.hitbox.center = self.rect.center

        self.animation_counter += 1
        if self.animation_counter > self.animation_cooldown:
            self.animation_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
        self.image = self.walk_frames[self.frame_index]
        if self.move_direction == 1:
            self.image = pygame.transform.flip(self.image, True, False)
