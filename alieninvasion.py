import sys
import pygame
from settings import Settings
from button import Button
from score import Scoreboard
from stats import GameStats
from ship import Ship
from pygame.sprite import Group
import gamefunctions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (230,230,230)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    playbutton = Button(ai_settings, screen, "playbutton")
    gf.create_fleet(ai_settings, screen, ship, aliens)
    statis = GameStats(ai_settings)
    scb = Scoreboard(ai_settings)
    bullets = Group()
    aliens = Group()
    while True:
        gf.check_events(ai_settings, statis, scb, playbutton ,ship, bullets, screen, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, playbutton)
        if statis.gane_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, statis, scb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, statis, screen, ship, aliens, bullets)
run_game()