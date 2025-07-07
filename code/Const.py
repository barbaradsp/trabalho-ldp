import pygame

# Dimensões
WIN_WIDTH = 395
WIN_HEIGHT = 648
TILE_SIZE = 36

# Física do jogo
GRAVITY = 0.75
PLAYER_SPEED = 2.3
JUMP_HEIGHT = -11.5

# Opções do menu
MENU_OPTION = ('INICIAR', 'SAIR')

# Cores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Legenda de tiles para o mapa
TILE_LEGEND = {
    1: './asset/castleCenter.png',
    2: './asset/castleMid.png',
    3: './asset/castleLeft.png',
    4: './asset/castleRight.png',
    5: './asset/castleHalf.png'
}
