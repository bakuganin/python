import pygame, os, time
pygame.init()

FPS = 60 # Задержка
clock = pygame.time.Clock()

#Наименование окна
pygame.display.set_caption( "Circle-4x4" )

#Установка окна
SCREEEN_SIZE = SIZE_X, SIZE_Y = 500, 500 # Переменные размера окна
gameDisplay = pygame.display.set_mode( ( SIZE_X,SIZE_Y ) ) # Создание окна

#Картежи цветов
WHITE = ( 255, 255, 255 ) # белый
BLACK = ( 0, 0, 0 ) # черный
GRAY = ( 125, 125, 125 ) # серый
LIGHT_BLUE = ( 64, 128, 255 ) # слегка синий
GREEN = ( 0, 200, 64 ) # зеленый
YELLOW = ( 225, 225, 0 ) # желтый
PINK = ( 230, 50, 230 ) # розовый
RED = ( 225, 0, 0 ) # красный
AQUA = ( 0, 255, 255 ) # аква-мариновый
TEAL = ( 0, 128, 128 ) # теплый	
NAVY = ( 0, 0, 128 ) # морской
SILVER = ( 192, 192, 192 ) # серебрянный 

#Списки(листы)
color = [WHITE, BLACK, GRAY, SILVER, LIGHT_BLUE, GREEN, YELLOW, PINK, RED, AQUA, TEAL, NAVY]

gameDisplay.fill( ( color[-5] ) ) # Заливка заднего фона цветом

#Размеры Rect()
rect_width = SIZE_X // 2
rect_height = SIZE_Y // 2
rect_size = ( rect_width, rect_height )

#Прямоугольные области на 4 чатси экрана программы
rect1 = pygame.Rect( ( 0, 0 ), rect_size )
rect2 = pygame.Rect( ( rect_width, 0 ), rect_size )
rect3 = pygame.Rect( ( 0, rect_height ), rect_size )
rect4 = pygame.Rect( ( rect_width, rect_height ), rect_size )

surf1 = pygame.Surface( rect_size )
surf2 = pygame.Surface( rect_size )
surf3 = pygame.Surface( rect_size )
surf4 = pygame.Surface( rect_size )

surf1.fill( color[1] )
surf2.fill( color[0] )
surf3.fill( color[0] )
surf4.fill( color[1] )

gameDisplay.blit( surf1, rect1 )
gameDisplay.blit( surf2, rect2 )
gameDisplay.blit( surf3, rect3 )
gameDisplay.blit( surf4, rect4 )

CIRCLE_COLOR = color[0]
circle_update = ( rect1, rect2, rect3, rect4 )

pygame.display.update()
Run = True # Пока переменная - "Run" = True цикл будет работать.
while Run:
	# Иницилизирует выход программы из цикла при нажание клавиши "ESC"
    for i in pygame.event.get():
        if i.type == pygame.QUIT or \
                i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
            exit()

        if i.type == pygame.KEYDOWN:
        	if i.key == pygame.K_1:
        		pygame.display.update()
        		circle_update = ( rect1, rect4 )
        		print("1")
        	elif i.key == pygame.K_2:
        		pygame.display.update()
        		circle_update = ( rect2, rect3 )
        		print("2")
        	elif i.key == pygame.K_0:
        		circle_update = ( rect1, rect2, rect3, rect4 )
        		print("0")
    if True:
    	if CIRCLE_COLOR == color[-0]:
    		CIRCLE_COLOR = color[1]
    		print("черный")
    	elif CIRCLE_COLOR == color[1]:
    		CIRCLE_COLOR = color[0]
    		print("белый")
    	pygame.draw.circle( gameDisplay, CIRCLE_COLOR, ( SIZE_X // 2, SIZE_Y // 2 ), 100 )
    	pygame.display.update( circle_update )
    	pygame.time.delay( 450 )


pygame.quit() #Иницилизирует, чтобы программа закрылась после выхода из цикла