import pygame
import random
from config import FAKE_LOVE_WIDTH, FAKE_LOVE_HEIGHT, FAKE_LOVE_VEL, WIDTH, HEIGHT, FAKE_LOVE_IMG

class FakeLove:
    def __init__(self):
        try:
            self.image = pygame.image.load(FAKE_LOVE_IMG).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image: {FAKE_LOVE_IMG} - {e}")
            self.image = pygame.Surface((FAKE_LOVE_WIDTH, FAKE_LOVE_HEIGHT))
            self.image.fill((255, 0, 0))  # Red placeholder
        
        self.image = pygame.transform.scale(self.image, (FAKE_LOVE_WIDTH, FAKE_LOVE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, max(0, HEIGHT - FAKE_LOVE_HEIGHT))
        self.vel = max(1, min(FAKE_LOVE_VEL, 10))  # Ensures velocity is reasonable

    def move(self):
        self.rect.x -= self.vel

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)
