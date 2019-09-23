import pygame
from pygame.sprite import Sprite
# 子弹类
class Bullet(Sprite):  # 精灵,可将游戏中相关的元素编组,进而同时操作编组中的所有元素

    def __init__(self , ai_settings, screen , ship):
        """在飞船所处位置创建一个子弹对象"""
        super(Bullet, self).__init__()

        self.screen = screen

        # 先创建一个子弹的初始矩形位置,在设置其位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width , ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动位置"""
        self.y -= self.speed_factor # 更新子弹位置
        self.rect.y = self.y # 更新表示子弹的rect的位置

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen , self.color , self.rect)