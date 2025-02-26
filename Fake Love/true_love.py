import pygame
import random
from config import TRUE_LOVE_WIDTH, TRUE_LOVE_HEIGHT, FAKE_LOVE_VEL, WIDTH, HEIGHT, TRUE_LOVE_IMG

class TrueLove:
    def __init__(self):
        try:
            self.image = pygame.image.load(TRUE_LOVE_IMG).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image: {TRUE_LOVE_IMG} - {e}")
            self.image = pygame.Surface((TRUE_LOVE_WIDTH, TRUE_LOVE_HEIGHT))
            self.image.fill((0, 255, 0))  # Green placeholder for True Love

        self.image = pygame.transform.scale(self.image, (TRUE_LOVE_WIDTH, TRUE_LOVE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, max(0, HEIGHT - TRUE_LOVE_HEIGHT))
        self.vel = FAKE_LOVE_VEL  # Consider using a separate TRUE_LOVE_VEL if needed

    def move(self):
        self.rect.x -= self.vel

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)
