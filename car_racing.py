"""
Author : Prathima Kadari
Date : 11th July 2021
"""

import random
from time import sleep

import pygame

class racingCar:
    def __init__(self):

        pygame.init()
        self.display_width = 900
        self.display_height = 700
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.initialize()

    def initialize(self):

        self.crashed = False

        self.imgCar = pygame.image.load('.\\Images\\Car.png')
        self.car_x_coordinate = (self.display_width * 0.45)
        self.car_y_coordinate = (self.display_height * 0.8)
        self.car_width = 45

        # enemy_car
        self.enemyCar = pygame.image.load('.\\Images\\Enemy_car.png')
        self.enemyCar_startx = random.randrange(320, 460)
        self.enemyCar_starty = -610
        self.enemyCar_speed = 4
        self.enemyCar_width = 48
        self.enemyCar_height = 90

        # Background
        self.bgImg = pygame.image.load(".\\Images\\background.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def car(self, car_x_coordinate, car_y_coordinate):
        self.displayGame.blit(self.imgCar, (car_x_coordinate, car_y_coordinate))

    def racingWindow(self):
        self.displayGame = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Race')
        self.runCar()

    def runCar(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                # print(event)

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.car_x_coordinate -= 50
                    if (event.key == pygame.K_RIGHT):
                        self.car_x_coordinate += 50

            self.displayGame.fill(self.black)
            self.backgroundRoad()

            self.run_enemyCar(self.enemyCar_startx, self.enemyCar_starty)
            self.enemyCar_starty += self.enemyCar_speed

            if self.enemyCar_starty > self.display_height:
                self.enemyCar_starty = 0 - self.enemyCar_height
                self.enemyCar_startx = random.randrange(300, 440)

            self.car(self.car_x_coordinate, self.car_y_coordinate)
            self.highScore(self.count)
            self.count += 1
            if (self.count % 100 == 0):
                self.enemyCar_speed += 1
                self.bg_speed += 1

            if self.car_y_coordinate < self.enemyCar_starty + self.enemyCar_height:
                if self.car_x_coordinate > self.enemyCar_startx and self.car_x_coordinate < self.enemyCar_startx + self.enemyCar_width or self.car_x_coordinate + self.car_width > self.enemyCar_startx and self.car_x_coordinate + self.car_width < self.enemyCar_startx + self.enemyCar_width:
                    self.crashed = True
                    self.displayMessage("Game Over !!!")

            if self.car_x_coordinate < 310 or self.car_x_coordinate > 460:
                self.crashed = True
                self.displayMessage("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)

    def displayMessage(self, msg):
        font = pygame.font.SysFont("Times New Roman", 70, True)
        text = font.render(msg, True, (255, 255, 255))
        self.displayGame.blit(text, (380 - text.get_width() // 2, 220 - text.get_height() // 2))
        self.displayCredit()
        pygame.display.update()
        self.clock.tick(70)
        sleep(1)
        car_racing.initialize()
        car_racing.racingWindow()

    def backgroundRoad(self):
        self.displayGame.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.displayGame.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemyCar(self, thingx, thingy):
        self.displayGame.blit(self.enemyCar, (thingx, thingy))

    def highScore(self, count):
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.displayGame.blit(text, (0, 0))

    def displayCredit(self):
        font = pygame.font.SysFont("Arial", 14)
        text = font.render("Regards,", True, self.white)
        self.displayGame.blit(text, (600, 520))
        text = font.render("Prathima Kadari", True, self.white)
        self.displayGame.blit(text, (600, 540))
        text = font.render("Developer", True, self.white)
        self.displayGame.blit(text, (600, 560))


if __name__ == '__main__':
    car_racing = racingCar()
    car_racing.racingWindow()