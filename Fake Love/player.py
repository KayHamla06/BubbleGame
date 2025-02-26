import pygame
from config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL, WIDTH, HEIGHT, PLAYER_IMG

class Player:
    def __init__(self):
        try:
            self.image = pygame.image.load(PLAYER_IMG).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image: {PLAYER_IMG} - {e}")
            self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
            self.image.fill((255, 0, 0))  # Red placeholder

        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - PLAYER_WIDTH // 2
        self.rect.y = HEIGHT // 2 - PLAYER_HEIGHT // 2
        self.vel = PLAYER_VEL
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.vel
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.vel
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.vel

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)
