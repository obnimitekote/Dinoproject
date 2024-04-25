import os
import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUN_CAT = [pygame.image.load(os.path.join("images/cat", "cat1.png"))]
DOWN_CAT = [pygame.image.load(os.path.join("images/cat", "cat2.png"))]

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

    def __init__(self):
        self.down_img = DOWN_CAT
        self.run_img = RUN_CAT
        self.jump_ing = RUN_CAT

        self.cat_down = False
        self.cat_run = True
        self.cat_jump = False

        self.image = self.run_img
        self.run_img.x = self.X_POS
        self.run_img.y = self.Y_POS


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((225,255,255))


main()