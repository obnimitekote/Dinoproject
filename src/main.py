import os
import random

import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUN_CAT = [pygame.image.load(os.path.join("images/cat", "catrun.png"))]
DOWN_CAT = [pygame.image.load(os.path.join("images/cat", "catdown.png"))]
JUMP_CAT = [pygame.image.load(os.path.join("images/cat", "catrun.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("images/cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("images/cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("images/cactus", "SmallCactus1.png"))]

BIG_CACTUS = [pygame.image.load(os.path.join("images/cactus", "LargeCactus1.png")),
              pygame.image.load(os.path.join("images/cactus", "LargeCactus2.png")),
              pygame.image.load(os.path.join("images/cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("images/bird", "Bird1.png")),
        pygame.image.load(os.path.join("images/bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("images/other", "Cloud.png"))

ROAD = pygame.image.load(os.path.join("images/other", "Track.png"))

class Cat():
    X_POS = 80
    Y_POS = 310
    Y_POS_DOWN = 315
    JUMP_VEL = 8.5

    def __init__(self):
        self.down_img = DOWN_CAT
        self.run_img = RUN_CAT
        self.jump_img = JUMP_CAT

        self.cat_down = False
        self.cat_run = True
        self.cat_jump = False

        self.step = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS

    def update(self, userInput):
        if self.cat_down:
            self.down()
        if self.cat_run:
            self.run()
        if self.cat_jump:
            self.jump()

        if userInput[pygame.K_SPACE] and not self.cat_jump:
            self.cat_down = False
            self.cat_run = False
            self.cat_jump = True
        elif userInput[pygame.K_DOWN] and not self.cat_jump:
            self.cat_down = True
            self.cat_run = False
            self.cat_jump = False
        elif not (self.cat_jump or userInput[pygame.K_DOWN]):
            self.cat_down = False
            self.cat_run = True
            self.cat_jump = False

    def down(self):
        self.image = self.down_img[0]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS_DOWN
        self.step += 1

    def run(self):
        self.image = self.run_img[0]
        self.cat_rect = self.image.get_rect()
        self.cat_rect.x = self.X_POS
        self.cat_rect.y = self.Y_POS
        self.step += 1

    def jump(self):
        self.image = self.jump_img[0]
        if self.cat_jump:
            self.cat_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.cat_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit (self.image, (self.cat_rect.x, self.cat_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(20, 50)
        self.y = random.randint(20, 50)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(10,20)
            self.y = random.randint(15, 90)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self,SCREEN):
        SCREEN.blit(self.image[self.type],self.rect)

class Smallobst(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class Bigobst(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Birdobst(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 245
        self.index = 0

    def draw(self,SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Cat()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death = 0


    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = font.render(f"Points: "+ str(points), True,(0,0,0))
        textRect = text.get_rect()
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = ROAD.get_width()
        SCREEN.blit(ROAD, (x_pos_bg, y_pos_bg))
        SCREEN.blit(ROAD, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(ROAD,(image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((225, 225, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Smallobst(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(Bigobst(BIG_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Birdobst(BIRD))


        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.cat_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                death += 1
                menu(death)


        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death):
    global points
    run = True
    while run:
        SCREEN.fill((200, 200, 225))
        font = pygame.font.Font("freesansbold.ttf",30)

        if death == 0:
            text = font.render("Press any Key to Start", True, (0,0,0))
        elif death > 0:
            text = font.render("Press any Key to Try Again", True, (0, 0, 0))
            score = font.render(f"Your Score: "+ str(points), True,(0,0,0))
            dead_message = font.render("You killed the cat", True, (200, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT //2 + 90)
            SCREEN.blit(score,scoreRect)
            dmRect = dead_message.get_rect()
            dmRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
            SCREEN.blit(dead_message, dmRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 140)
        SCREEN.blit(text,textRect)
        SCREEN.blit(DOWN_CAT[0], (SCREEN_WIDTH // 2-20, SCREEN_HEIGHT // 2-110))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                    main()

menu(death=0)