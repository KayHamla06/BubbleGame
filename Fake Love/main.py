import pygame
import time
import random
from config import WIDTH, HEIGHT, LIVES, LOGO_DURATION, BG_IMG_LIST
from player import Player
from fake_love import FakeLove
from true_love import TrueLove
from utils import load_image, draw_window, display_logo
from sound import play_collision_sound, play_win_sound, toggle_music

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fake Love")

BG_INDEX = 0
BG = load_image(BG_IMG_LIST[BG_INDEX], WIDTH, HEIGHT)
LOGO = load_image("bubbleGame.png", WIDTH, HEIGHT)
FONT = pygame.font.SysFont("comicsans", 30)

def draw_homepage():
    """Draws the homepage with Start and Quit buttons."""
    WIN.fill((0, 0, 0))  
    font = pygame.font.SysFont("comicsans", 50)
    title_text = font.render("Fake Love Game", True, "white")
    WIN.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 150))
    
    start_button = pygame.Rect(WIDTH / 2 - 100, 300, 200, 50)
    quit_button = pygame.Rect(WIDTH / 2 - 100, 400, 200, 50)
    
    pygame.draw.rect(WIN, "green", start_button)
    pygame.draw.rect(WIN, "red", quit_button)
    
    button_font = pygame.font.SysFont("comicsans", 35)
    start_text = button_font.render("Start Game", True, "black")
    quit_text = button_font.render("Quit Game", True, "black")
    
    WIN.blit(start_text, (start_button.x + 35, start_button.y + 10))
    WIN.blit(quit_text, (quit_button.x + 35, quit_button.y + 10))
    
    pygame.display.flip()  # Optimize rendering
    return start_button, quit_button

def home_page():
    while True:
        start_button, quit_button = draw_homepage()
        for event in pygame.event.get():  # Corrected from pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return  # Start the game
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

def switch_background():
    """Cycles through background images."""
    global BG_INDEX, BG
    BG_INDEX = (BG_INDEX + 1) % len(BG_IMG_LIST)
    BG = load_image(BG_IMG_LIST[BG_INDEX], WIDTH, HEIGHT)

def pause_screen():
    """Displays the pause screen instead of freezing the game."""
    pause_font = pygame.font.SysFont("comicsans", 50)
    pause_text = pause_font.render("Paused - Press P to Resume", True, "white")
    WIN.blit(pause_text, (WIDTH / 2 - pause_text.get_width() / 2, HEIGHT / 2))
    pygame.display.flip()  # Update only the changed area

def main():
    home_page()  
    run = True
    clock = pygame.time.Clock()
    player = Player()
    fake_loves, true_loves = [], []
    score, start_time, star_count = 0, time.time(), 0
    paused = False

    display_logo(WIN, LOGO, LOGO_DURATION)

    while run:
        clock.tick(60)

        # Background change logic (every 10 seconds)
        if time.time() - start_time > 10:
            switch_background()
            start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_m:
                    toggle_music()

        if paused:
            pause_screen()
            continue  # Skip updating game state while paused

        # Generate Fake Loves and True Loves randomly
        if random.randint(1, 50) == 1:  # 1 in 50 chance per frame
            fake_loves.append(FakeLove())
        if random.randint(1, 100) == 1:  # 1 in 100 chance per frame
            true_loves.append(TrueLove())

        keys = pygame.key.get_pressed()
        player.move(keys)

        for fake_love in fake_loves[:]:
            fake_love.move()
            if fake_love.rect.right < 0:
                fake_loves.remove(fake_love)
            elif fake_love.rect.colliderect(player.rect):
                fake_loves.remove(fake_love)
                player.lives -= 1
                play_collision_sound()
                if player.lives <= 0:
                    WIN.fill((0, 0, 0))
                    game_over_text = FONT.render("Game Over! Fake Love Caught You!", True, "red")
                    WIN.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, HEIGHT / 2))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    return  # End game

        for true_love in true_loves[:]:
            true_love.move()
            if true_love.rect.right < 0:
                true_loves.remove(true_love)
            elif true_love.rect.colliderect(player.rect):
                true_loves.remove(true_love)
                score += 5  # Gain points
                play_win_sound()

        draw_window(WIN, BG, player, fake_loves, true_loves, time.time() - start_time, score, player.lives)

    pygame.quit()

if __name__ == "__main__":
    main()
