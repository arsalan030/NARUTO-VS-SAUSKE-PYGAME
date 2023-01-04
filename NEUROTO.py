import pygame


pygame.init()

"first we make the window of the game"
win = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Naruto vs Sasuke")
'"then we give caption of the window by  name of game  "'

walk_Right = [pygame.image.load("pics\\NR2.png"), pygame.image.load('pics\\NR3.png'),
              pygame.image.load('pics\\NR1.png')]
walk_Left = [pygame.image.load("pics\\NL2.png"), pygame.image.load('pics\\NL3.png'), pygame.image.load('pics\\NL1.png')]

bg = pygame.image.load('pics\\bg.png')
stan = pygame.image.load('pics\\Nstanding.png')
sh = pygame.image.load('pics\\Sh.png')
Nh = pygame.image.load('pics\\Nh.png')
hitsound= pygame.mixer.Sound('pics\\hit.wav')
bgm=pygame.mixer.music.load('pics\\a-hero-of-the-80s-126684.wav')

pygame.mixer.music.play()


pygame.time.Clock()


class Player:
    def __init__(self, x, y, hight, width):
        self.x = x
        self.y = y
        self.hight = hight
        self.width = width
        self.speed = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump_hieght = 10
        self.isjump = False
        self.standing = True
        self.hitbox = (self.x + 10, self.y + 5, 80, 80)
        self.health = 200

    def draw(self, win):
        if self.health > 0:
            if self.walk_count + 1 > 6:
                self.walk_count = 0
            if not (self.standing):
                if self.left:
                    win.blit(walk_Left[self.walk_count // 2], (self.x, self.y))
                    self.walk_count += 1
                elif self.right:
                    win.blit(walk_Right[self.walk_count // 2], (self.x, self.y))
                    self.walk_count += 1
            else:
                if self.right:
                    win.blit(pygame.image.load('pics\\NR1.png'), (self.x, self.y))
                else:
                    win.blit(pygame.image.load('pics\\Nl1.png'), (self.x, self.y))
            self.hitbox = (self.x + 10, self.y + 5, 80, 80)
            nbar_2 = pygame.draw.rect(win, (255, 0, 0), (80, 45, 200, 20))
            nbar = pygame.draw.rect(win, (255, 255, 0), (80, 45, self.health, 15))
        else:
            win.blit(pygame.image.load('pics\\loss.png'), (180,200))
            win.blit(pygame.image.load('pics\\Nd.png'), (self.x, self.y))

    def hit(self):
        if self.health > 0:
            self.health -= 5
        else:
            print("naruto died")


class weapon:
    def __init__(self, x, y, hight, width, facing):
        self.x = x
        self.y = y
        self.hight = hight
        self.width = width
        self.facing = facing
        self.vel = 8 * facing
        self.standing = True
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self, win):
        win.blit(pygame.image.load('pics\\shur.png'), (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 40)


class Enemy:
    walk_Righs = [pygame.image.load("pics\\SR2.png"), pygame.image.load('pics\\SR3.png'),
                  pygame.image.load('pics\\SR1.png')]
    walk_Lefts = [pygame.image.load("pics\\SL2.png"), pygame.image.load('pics\\SL3.png'),
                  pygame.image.load('pics\\SL1.png')]

    def __init__(self, x, y, hight, width, end):
        self.x = x
        self.y = y
        self.hight = hight
        self.width = width
        self.end = end
        self.path = [self.x, self.end]
        self.speed = 8
        self.walkcount = 0
        self.hitbox = (self.x + 10, self.y + 5, 80, 80)
        self.health = 200

    def draw(self, win):
        if sasuke.health > 0:
            self.move()
            if self.walkcount + 1 >= 6:
                self.walkcount = 0
            if self.speed > 0:
                win.blit(self.walk_Righs[self.walkcount // 2], (self.x, self.y))
                self.walkcount += 1
            else:
                win.blit(self.walk_Lefts[self.walkcount // 2], (self.x, self.y))
                self.walkcount += 1
            self.hitbox = (self.x + 10, self.y + 5, 80, 80)
            sbar_2 = pygame.draw.rect(win, (255, 0, 0), (410, 45, 210, 20))
            sbar = pygame.draw.rect(win, (255, 255, 0), (410, 45, self.health, 15))
        else:
            win.blit(pygame.image.load('pics\\win.png'), (180, 200))
            win.blit(pygame.image.load("pics\\Sd.png"), (self.x, self.y))

    def move(self):
        if self.speed > 0:
            if self.speed + self.x < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkcount = 0
        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkcount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 5
        else:
            print("sauske died")


run = True


def ReDraw_Game_Window():
    win.blit(bg, (0, 0))
    naruto.draw(win)
    sasuke.draw(win)
    font=pygame.font.SysFont('comicsans',60,True)
    win.blit(sh, (600, 10))
    win.blit(Nh, (10, 10))

    for shurikene in shurikenes:
        shurikene.draw(win)

    pygame.display.update()


naruto = Player(30, 400, 100, 100)
sasuke = Enemy(100, 400, 100, 100, 600)

shurikenes = []
throw_speed = 0

while run:
    """Start the main loop for the game."""
    pygame.time.delay(30)
    if throw_speed > 0:
        throw_speed += 1
    if throw_speed > 3:
        throw_speed = 0

    ############# keys   ################
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False

    if naruto.health > 0 and sasuke.health > 0:
        if naruto.hitbox[1] < sasuke.hitbox[1] + sasuke.hitbox[3] and naruto.hitbox[1] + naruto.hitbox[3] > \
                sasuke.hitbox[1]:
            if naruto.hitbox[0] + naruto.hitbox[2] > sasuke.hitbox[0] and naruto.hitbox[0] < sasuke.hitbox[0]+sasuke.hitbox[2]:
                naruto.hit()
                hitsound.play()
    else:
        if naruto.health == 0:
            naruto.speed = 0

    for shurikene in shurikenes:
        if sasuke.health > 0:
            if shurikene.hitbox[1] + round(shurikene.hitbox[3] / 2) > sasuke.hitbox[1] and shurikene.hitbox[1] + round(
                    shurikene.hitbox[3] / 2) < sasuke.hitbox[1] + sasuke.hitbox[3]:
                if shurikene.hitbox[0] + shurikene.hitbox[2] > sasuke.hitbox[0] and shurikene.hitbox[0] + \
                        shurikene.hitbox[
                            2] < sasuke.hitbox[0] + sasuke.hitbox[2]:
                    sasuke.hit()
                    hitsound.play()
                    shurikenes.pop(shurikenes.index(shurikene))
        else:
            sasuke.speed = 0
        if shurikene.x < 699 and shurikene.x > 0:
            shurikene.x += shurikene.vel
        else:
            shurikenes.pop(shurikenes.index(shurikene))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if naruto.left == True:
            facing = -1
        else:
            facing = 1
        if len(shurikenes) < 5:
            shurikenes.append(
                weapon(round(naruto.x+60), round(naruto.y + 30), 40, 40, facing))

        throw_speed = 1

    ######################  LEFT #################
    if keys[pygame.K_LEFT] and naruto.x > naruto.speed:
        naruto.x -= naruto.speed
        naruto.left = True
        naruto.right = False
        naruto.standing = False

    ################### RIGHT ###################
    elif keys[pygame.K_RIGHT] and naruto.x < 690 - naruto.width:
        naruto.x += naruto.speed
        naruto.right = True
        naruto.left = False
        naruto.standing = False

    else:
        naruto.standing = True
        naruto.walk_count = 0

    ############## JUMP ###################
    if naruto.isjump == False:
        if keys[pygame.K_UP]:
            naruto.isjump = True
            naruto.left = False
            naruto.right = False
            naruto.walk_count = 0
            naruto.standing = False
    else:
        naruto.standing = True
        if naruto.jump_hieght >= -10:
            neg = 1
            if naruto.jump_hieght < 0:
                neg = -1
            naruto.y -= (naruto.jump_hieght ** 2) * 0.5 * neg
            naruto.jump_hieght -= 1
        else:
            naruto.isjump = False
            naruto.jump_hieght = 10

    ReDraw_Game_Window()

pygame.quit()

