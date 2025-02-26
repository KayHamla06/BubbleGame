import pygame
from config import COLLISION_SOUND, WIN_SOUND, BG_MUSIC

pygame.mixer.init()

# Load background music
bg_music = pygame.mixer.Sound(BG_MUSIC)
bg_music.set_volume(0.5)  # Adjust default volume
bg_music.play(-1)  # Loop indefinitely

# Preload sound effects
collision_sound = pygame.mixer.Sound(COLLISION_SOUND)
win_sound = pygame.mixer.Sound(WIN_SOUND)

def play_collision_sound():
    collision_sound.play()

def play_win_sound():
    win_sound.play()

def toggle_music():
    if bg_music.get_volume() > 0:
        bg_music.set_volume(0)  # Mute
    else:
        bg_music.set_volume(1)  # Unmute

def stop_music():
    """Stops background music (useful when quitting game)."""
    bg_music.stop()
