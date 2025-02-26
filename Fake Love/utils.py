import pygame
from config import FONT_SIZE

def load_image(path, width=None, height=None):
    """Loads an image with optional scaling. Prevents crashes on missing files."""
    try:
        img = pygame.image.load(path)
        if width and height:
            img = pygame.transform.scale(img, (width, height))
        return img
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")
        return None  # Prevents crashes if image fails to load

def draw_window(win, bg, player, fake_loves, true_loves, elapsed_time, score, lives):
    """Draws the game screen with all elements."""
    win.blit(bg, (0, 0))
    player.draw(win)
    
    for fake_love in fake_loves:
        fake_love.draw(win)
    for true_love in true_loves:
        true_love.draw(win)

    font = pygame.font.SysFont("comicsans", FONT_SIZE)
    win.blit(font.render(f"Time: {round(elapsed_time)}s", 1, "white"), (10, 10))
    win.blit(font.render(f"Score: {score}", 1, "white"), (10, 40))
    win.blit(font.render(f"Lives: {lives}", 1, "red"), (10, 70))

    pygame.display.flip()  # Optimized screen update

def display_logo(win, logo, duration):
    """Displays the game logo for a given duration without freezing the game."""
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration:
        win.blit(logo, (0, 0))
        pygame.display.update()
