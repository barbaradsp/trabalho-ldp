import pygame
from code.Const import *
from code.World import Platform


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.walk_frames = []
        self.frame_index = 0
        self.direction = 1
        self.animation_counter = 0
        self.walk_cooldown = 4

        for i in range(1, 12):
            img_original = pygame.image.load(f'./asset/p3_walk{i:02d}.png').convert_alpha()
            new_width = int(TILE_SIZE * 0.9)
            original_width, original_height = img_original.get_size()
            aspect_ratio = original_height / original_width
            new_height = int(new_width * aspect_ratio)
            img_scaled = pygame.transform.scale(img_original, (new_width, new_height))
            self.walk_frames.append(img_scaled)

        self.image = self.walk_frames[self.frame_index]
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.hitbox = self.rect.inflate(int(TILE_SIZE * -0.3), -10)

        self.vel_y = 0
        self.jumped = False
        self.on_ground = False

    def _handle_animation(self, is_moving):
        if is_moving:
            self.animation_counter += 1
            if self.animation_counter > self.walk_cooldown:
                self.animation_counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
        else:
            self.frame_index = 0

        clean_image = self.walk_frames[self.frame_index]
        if self.direction == -1:
            self.image = pygame.transform.flip(clean_image, True, False)
        else:
            self.image = clean_image

    def update(self, world_tiles, moving_platforms, enemies_group, lava_group):
        dx = 0
        dy = 0
        is_moving = False
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and not self.jumped and self.on_ground:
            self.vel_y = JUMP_HEIGHT
            self.jumped = True
        if key[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
            self.direction = -1
            is_moving = True
        if key[pygame.K_RIGHT]:
            dx = PLAYER_SPEED
            self.direction = 1
            is_moving = True

        self.vel_y += GRAVITY
        if self.vel_y > 10: self.vel_y = 10
        dy += self.vel_y

        self.on_ground = False
        all_platforms = world_tiles + list(moving_platforms)
        for tile in all_platforms:
            if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y < 0:
                    dy = tile.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile.rect.top - self.rect.bottom
                    self.vel_y = 0
                    self.on_ground = True
                    self.jumped = False
                    if isinstance(tile, Platform):
                        self.rect.x += tile.move_direction * tile.speed

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

        self.hitbox.center = self.rect.center

        self._handle_animation(is_moving)

        for enemy in enemies_group:
            if enemy.hitbox.colliderect(self.hitbox):
                return 'game_over'
        for lava_tile in lava_group:
            if lava_tile.hitbox.colliderect(self.hitbox):
                return 'game_over'
        if self.rect.top > WIN_HEIGHT:
            return 'game_over'

        return 'playing'
