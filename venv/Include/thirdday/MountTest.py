import pygame

bg_img_file = "sea.jpg"
SCREEN_SIZE = (1208 , 720)
pygame.init()

pygame.display.set_caption("鼠标移动")
"""
创建一个窗口,set_mode返回一个Surface对象,代表在桌面上出现的那个窗口
第一个参数为元组,代表分辨率
第二个是一个标志位,指定为0 ,如果设置成FULLSCREEN时,得到一个全屏窗口
第三个为色深
"""
screen = pygame.display.set_mode(SCREEN_SIZE , 0 , 32)
backgroudImg = pygame.image.load(bg_img_file).convert() # 加载并转换图片

x, y = 0 , 0
move_x , move_y = 0 , 0

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                move_x = -1
            elif event.key == pygame.K_RIGHT:
                move_x = 1
            elif event.key == pygame.k_UP:
                move_y = -1
            elif event.key == pygame.k_DOWN:
                move_y = 1
        elif event.type == pygame.KEYUP:
            move_x = 0
            move_y = 0

    x += move_x
    y += move_y

    screen.fill((0,0,0))
    screen.blit(backgroudImg , (x , y))
    # 在新位置画图
    pygame.display.update()




