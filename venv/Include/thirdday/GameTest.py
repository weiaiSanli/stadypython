import pygame
from pygame.locals import *
from sys import exit

backg_img_fileName = "sea.jpg"
mouse_img_fileName = "mouse.jpg"

pygame.init()

screen = pygame.display.set_mode((640, 480) , 0 , 32)

pygame.display.set_caption("nihao a ")

bgImg = pygame.image.load(backg_img_fileName)
mouse_curson = pygame.image.load(mouse_img_fileName)


while True:
    for event in pygame.event.get():
        if event.type == quit:
            # 接收到退出时间后退出程序
            exit()
        # 将背景图画上去
        screen.blit(bgImg, (0, 0))

        # 获得鼠标位置
        x, y = pygame.mouse.get_pos()
        # 计算光标左上角位置
        x -= mouse_curson.get_width() / 2
        y -= mouse_curson.get_height() / 2

        # 将光标画上去
        screen.blit(mouse_curson, (x, y))

        # 刷新画面
        pygame.display.update()


