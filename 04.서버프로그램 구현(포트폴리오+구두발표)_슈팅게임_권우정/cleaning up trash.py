
# music by https://freemusicarchive.org/music/sawsquarenoise
# game asset by https://opengameart.org/content/2d-space-assets-set


import pygame
import random
import os
import sys
import time

# ----- 게임창 위치설정 -----

win_posx = 700
win_posy = 300
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (win_posx, win_posy)

image_dir = os.path.join(os.path.dirname(__file__), 'img')
sound_dir = os.path.join(os.path.dirname(__file__), 'sfx')
print(image_dir)


# ----- 전역 -----

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 60

score = 0
playtime = 1

# ----- 색상 -----

BLACK = 0, 0, 0
WHITE = 255,255,255
RED = 255, 0, 0
GREEN1 = 25, 102, 25
GREEN2 = 51, 204, 51
GREEN3 = 233, 249, 185
BLUE = 17, 17, 212
BLUE2 = 0, 0, 255
YELLOW = 255, 255, 0
LIGHT_PINK1 = 255, 230, 255
LIGHT_PINK2 = 255, 204, 255

def initialize_game(width, height):
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("CLEANING UP TRASH")
    return surface

def game_loop(surface):

    # ----- load game graphics -----

    background = pygame.image.load(os.path.join(image_dir, 'OceanBackground_pixel.jpg')).convert()
    bg_rect = background.get_rect()
    player_image = pygame.image.load(os.path.join(image_dir, 'dolphin_110150.png')).convert()
    bullet_image = pygame.image.load(os.path.join(image_dir, 'water drop_3040.png')).convert()
    start_image = pygame.image.load(os.path.join(image_dir, 'startimage_2.jpg')).convert()
    # gameover_image = pygame.image.load(os.path.join(image_dir, 'gameover_1.png')).convert()
    asteroid_image = []
    asteroid_list = ['trash01_pixel.png', 'trash02_pixel.png', 'trash03_pixel.png', 'trash04_pixel.png', 'trash05_pixel.png']
    for img in asteroid_list:
        asteroid_image.append(pygame.image.load(os.path.join(image_dir, img)).convert())

    shoot_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'missile.wav'))
    shoot_sound.set_volume(0.1)
    explosion_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'explosion_01.wav'))
    explosion_sound.set_volume(0.1)

    pygame.mixer.music.load(os.path.join(sound_dir, 'music.mp3'))
    pygame.mixer.music.set_volume(4)
    pygame.mixer.music.play(loops=-1)

    clock = pygame.time.Clock()
    sprite_group = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = PlayerShip(player_image)
    global player_health
    player_health= 100
    global score
    score = 0
    sprite_group.add(player)
    for i in range(7):
        enemy = Mob(asteroid_image)
        sprite_group.add(enemy)
        mobs.add(enemy)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            screen.blit(start_image, (0, 0))
        font = pygame.font.Font('NanumSquareRoundEB.ttf', 48)
        text1 = font.render('CLEANING UP', True, BLUE)
        screen.blit(text1, (95, 280))
        text2 = font.render('TRASH', True, BLUE)
        screen.blit(text2, (173, 330))
        font = pygame.font.Font('NanumSquareRoundEB.ttf', 28)
        text3 = font.render('SHOOTING GAME', True, BLACK)
        screen.blit(text3, (142, 385))
        font = pygame.font.Font('NanumSquareRoundEB.ttf', 30)
        text3 = font.render('PRESS ENTER TO START', True, RED)
        screen.blit(text3, (83, 440))
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_SPACE:
                    player.shoot(sprite_group, bullets, bullet_image, shoot_sound)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(sprite_group, bullets, bullet_image, shoot_sound)


        sprite_group.update()

        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            explosion_sound.play()
            mob = Mob(asteroid_image)
            sprite_group.add(mobs)
            mobs.add(mob)
            score += 10

        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            print('a mob hits player!')
            player_health -= 1
            if player_health < 0:
                gameover(surface)
                close_game()
                # restart()


        surface.fill(BLACK)
        surface.blit(background, bg_rect)
        sprite_group.draw(surface)
        score_update(surface)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    print('game played: ', playtime)

def score_update(surface):
    # font = pygame.font.SysFont('NanumSquareRoundEB.ttf', 35)
    font = pygame.font.Font('NanumSquareRoundEB.ttf', 40)
    image = font.render(f'  점수 : {score} / HP: {player_health} ', True, RED)
    pos = image.get_rect()
    pos.move_ip(20, 20)
    pygame.draw.rect(image, YELLOW, (pos.x-20, pos.y-20, pos.width, pos.height), 5)
    surface.blit(image, pos)

def gameover(surface):
    # font = pygame.font.SysFont('malgungothic',80)
    # font = pygame.font.Font('NanumSquareRoundEB.ttf', 80)
    # image = font.render('GAME OVER', True, RED)
    gameover_image = pygame.image.load(os.path.join(image_dir, 'gameover_4.png')).convert()
    start_image = pygame.image.load(os.path.join(image_dir, 'startimage_2.jpg')).convert()
    screen.blit(gameover_image, (100, 250))
    pos = gameover_image.get_rect()
    pos.move_ip(20, int(SCREEN_HEIGHT/2)-30)
    # surface.blit(image, pos)
    font = pygame.font.Font('NanumSquareRoundEB.ttf', 30)
    text5 = font.render('PRESS ENTER TO RESTART', True, RED)
    screen.blit(text5, (50, 445))
    # surface.blit(image, pos)
    pygame.display.update()
    time.sleep(2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    game_loop(surface)



def close_game():
    pygame.quit()
    print('Game closed')

def restart():
    screen = initialize_game(SCREEN_WIDTH,SCREEN_HEIGHT)
    game_loop(screen)
    close_game()

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((40,30))
        self.image = pygame.transform.scale(image, (110, 150))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9/2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius, 1)
        # self.image.fill(RED)
        self.rect.centerx = int(SCREEN_WIDTH / 2)
        self.rect.centery = SCREEN_HEIGHT - 20
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self, all_sprites,bullets, image, sound):
        bullet = Bullet(self.rect.centerx, self.rect.top, image)
        all_sprites.add(bullet)
        bullets.add(bullet)
        sound.play()


class Mob(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image_origin = random.choice(image)
        self.image_origin = pygame.transform.rotozoom(random.choice(image), 0, 0.7)


        self.image = self.image_origin
        self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((30,30))
        # self.color = random.choice([RED, BLUE, RED, GREEN1, YELLOW])
        # self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius, 1)
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange( 1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rotation = 0
        self.rotation_speed = random.randrange(-10, 10)
        # self.rotation_speed = 7
        self.last_update = pygame.time.get_ticks()


    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_origin, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (30, 40))
        self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((10,20))
        # self.image.fill(GREEN1)
        self.rect = self.image.get_rect()
        # pygame.draw.ellipse(self.image, RED, self.rect,1)
        self.rect.bottom = player_y
        self.rect.centerx = player_x
        self.speedy = - 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

if __name__ == '__main__':
    screen = initialize_game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game_loop(screen)
    sys.exit()

