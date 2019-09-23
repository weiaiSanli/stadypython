import sys

import pygame

from Include.game.alien import Alien
from Include.game.bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydowm_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:  # 向右移动飞船
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)

    elif event.key == pygame.K_q:
        sys.exit()


# 创建一颗子弹,并将其加入到编组bullets中
def fire_bullet(bullets, ai_settings, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 在飞船和外星人后面重绘所有子弹

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置并删除以消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)

    for alien_number in range(number_aliens_x):
        # 创建一个外星人并将其加入当前行
        create_alien(ai_settings, screen, aliens, alien_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_aliens_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_aliens_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
