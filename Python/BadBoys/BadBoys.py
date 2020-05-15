import pygame, random, sys, time, pyglet, ctypes
pygame.init()

#Цвета
plum = (221, 160, 221)
pink = (230, 50, 230)
navy = (0, 0, 128)
light_blue = (64, 128, 255)
gray = (119, 118, 110)
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
aqua = (0, 128, 255)

FPS = 33
SIZE_WIN = window_width, window_hight = 728, 455
yo = [-100]
yg = [-1000]
pause = False

max_flare = 5
flare_size = 500

pygame.mixer.init()
crash_sound = pygame.mixer.Sound('sounds\crash.wav')

pygame.mixer.music.load('sounds\carm.wav')


gameIcon = pygame.image.load('Texture\caricon.png')
pygame.display.set_icon(gameIcon)

#Окно
gd = pygame.display.set_mode((window_width,window_hight))
carimg = pygame.image.load('Texture\maincar.png')
car1 = pygame.transform.scale(carimg,(65,130))
clock = pygame.time.Clock()

class Flare():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_y = random.randint(2, 6)
        self.speed_x = random.randint(-1, 3) / 2
        self.imgNum = random.randint(1,11)
        self.image_filename = (("Texture\\flare\\") + str(self.imgNum) + '.png')
        self.image = pygame.image.load(self.image_filename).convert_alpha()


    def move_flare(self):
        self.y += self.speed_y
        if self.y > window_hight:
            self.y = (0 - flare_size)

        self.x += self.speed_x

        if self.x >= window_width:
            self.x = (0 - flare_size)
        elif self.x <= 0:
            self.x = window_width

    def draw_flare(self):
        gd.blit(self.image, (self.x, self.y))


def i_flare(max_flare, flarefall):
    for i in range(0, max_flare):
        xx = random.randint(0, window_width)
        yy = random.randint(0, window_hight)
        flarefall.append(Flare(xx, yy))
        print(xx, yy)



def load(name, x_pos, y_pos):
    v = pygame.image.load(name)
    gd.blit(v, (x_pos, y_pos))
    pygame.display.update()
    
def message(mess, colour, size, x, y):
     font = pygame.font.SysFont(None, size)
     screen_text = font.render(mess, True, colour)
     gd.blit(screen_text,(x, y))


def button(x, y, w, h, mess, mess_color, actc, noc, size, tx, ty, func):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gd, actc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        if click == (1, 0, 0):
            func()
    else:
        pygame.draw.rect(gd, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
    
def quit1():
    pygame.quit()
    quit()

def game_intro():
  backg_surf = pygame.image.load('Texture\Background1.jpg')
  backg_rect = backg_surf.get_rect()
  time.sleep(1)
  gameintro = False
  pygame.mixer.music.play(-1)
  time.sleep(1)
  while gameintro == False:
    gd.blit(backg_surf, backg_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameintro = True
            game_over = True
            
    window_width = 800
    window_hight = 600

    for i in flarefall:
      i.move_flare()
      i.draw_flare()
    time.sleep(0.030)

    message('BAD MENU', pink, 100,(window_width // 2 - 235), 100)
    button(100, 350, 70, 30, 'START', plum, white, black, 25, 108, 356, gameloop)
    button(550, 350, 70, 30, 'EXIT', plum, white, black, 25, 565, 356, quit1)
    pygame.display.update()
    clock.tick(75)

def unpause():
    pygame.mixer.music.unpause()
    time.sleep(0.1)
    global pause
    pause = False
    
def paused():
    backg_surf = pygame.image.load('Texture\Background1.jpg')
    backg_rect = backg_surf.get_rect()
    pygame.mixer.music.pause()
    time.sleep(0.1)
    while pause:
        gd.blit(backg_surf, backg_rect)
        message("   PAUSED", pink, 100, (window_width // 2 - 205), 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    time.sleep(0.1)
                    unpause()

        button(100, 350, 105, 30, 'CONTINUE', plum, white, black, 25, 108, 356, unpause)
        button(550, 350, 70, 30, 'EXIT', plum, white, black, 25, 565, 356, quit1)

        pygame.display.update()
        clock.tick(15)  

def grass(y_gr):
    gd.fill(gray)
    grassSurf_left = pygame.image.load('Texture\grass1.jpg')
    grassSurf_right = pygame.image.load('Texture\grass2.jpg')
    img = pygame.transform.scale(grassSurf_left,(100, 2000))
    img2 = pygame.transform.scale(grassSurf_right,(100, 2000))
    clock.tick(9999999)
    global  x_gr

    if y_gr == -1000:
        x_gr = 0
        yg.clear()
        yg.append(x_gr)
        y_gr += 0
    else:
        x_gr = yg[0]
        gd.blit(img,(x_gr, y_gr))
        gd.blit(img2,(628, y_gr))

def crash(x):    
    if 80 > x or x + 60 > 645:
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('SLOWDOWN', True, bright_red)
        gd.blit(screen_text, (145, 180))

def car_crash(x, y, y_en, x_en):
    if x < x_en + 57 < x + 105 and (y < y_en + 88 < y + 88 or y < y_en < y + 100):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        message('  WASTED!', red, 75, 215, 200)
        x_en = random.randrange(100, 600)
        yo.clear()
        yo.append(x_en)
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, white)
    gd.blit(screen_text, (550, 0))


def other_car(y_en):
    enmy1 = pygame.image.load('Texture\enemy.png')
    enmy = pygame.transform.scale(enmy1,(70, 100))
    global  x_en
    
    if y_en == -100:
        x_en = random.randrange(100, 500)
        yo.clear()
        yo.append(x_en)
        y_en += 2
    else:
        x_en = yo[0]
        gd.blit(enmy,(x_en, y_en))



def gameloop():
     global pause, game_over
     pygame.mixer.music.play(-1)
     x = 300
     y = 400
     speed = 2
     speed_en = 3
     x_change = 0
     y_change = 0
     game_over = False
     count = 0
     y_en = 1
     y_gr = -1000
     while game_over == False:
         speed += 0.01
         speed_en += 0.001
         for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     game_over = True
                     quit1()
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                         x_change = -speed
                     elif event.key == pygame.K_RIGHT:
                         x_change = +speed
                     elif event.key == pygame.K_ESCAPE:
                         pause = True
                         paused()
                 if event.type == pygame.KEYUP:
                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                         x_change=0
         gd.fill(gray)
         x += x_change
         grass(y_gr)
         gd.blit(car1, (x, y))
         if y_en > 465:
             y_en = -100
             count += 1
         if y_gr > -10:
             y_gr = -1210
         if 80 > x or x + 60 > 645:
             if speed >= 2:
                 speed -= 0.015
         other_car(y_en)
         y_en += speed_en
         y_gr += speed_en + 1
         crash(x)
         car_crash(x, y , y_en, x_en)
         score(count)
         clock.tick(60)
         pygame.display.update()


x_en = random.randrange(100, 600)
yo.clear()
yo.append(x_en)
flarefall = []
i_flare(max_flare, flarefall)
game_intro()
quit1()
