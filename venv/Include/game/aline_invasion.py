import pygame
import sys

from pygame.sprite import Group

from Include.game.Settings import Settings
from Include.game.alien import Alien
from Include.game.ship import Ship
import Include.game.game_functions as gf

backg_img_fileName = "sea.jpg"


def run_game():
    pygame.init()  # 初始化pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings , screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建一个外星人
    alien = Alien(ai_settings , screen)

    gf.create_fleet(ai_settings , screen , aliens)

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        """更新子弹位置并删除消失的子弹"""
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings , screen , ship , aliens ,  bullets)

run_game()
