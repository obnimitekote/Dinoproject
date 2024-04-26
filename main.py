import os
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
    Y_POS_DOWN = 340
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

        if userInput[pygame.K_UP] and not self.cat_jump:
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

def main():
    run = True
    clock = pygame.time.Clock()
    player = Cat()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((225, 225, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()

main()
