import random

import pygame

from file_helper import *

class Player:
    def __init__(self, speed,
                 x, y,
                 width, height,
                 skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.bullets = []
    def draw(self, window):
        window.blit(self.skin, self.hitbox)
        for bullet in self.bullets:
            bullet.draw(window)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.hitbox.x < 650:
            self.hitbox.x += self.speed
        if keys[pygame.K_a] and self.hitbox.x > 0:
            self.hitbox.x -= self.speed
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(10, self.hitbox.x + 10, self.hitbox.y, 10, 20, "photo/bullet (1).png"))

        for bullet in self.bullets:
            bullet.update()


class Enemy:
    def __init__(self, speed,
                 x, y,
                 width, height,
                 skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
    def draw(self, window):
        window.blit(self.skin, self.hitbox)

    def update(self):
        self.hitbox.y += self.speed
        if self.hitbox.y > 500:
            self.hitbox.y = -100
            self.hitbox.x = random.randint(0, 600)

class Bullet:
    def __init__(self, speed,
                 x, y,
                 width, height,
                 skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.bullets = []

    def draw(self, window):
        window.blit(self.skin, self.hitbox)

    def update(self):
        self.hitbox.y -= self.speed

pygame.init()
window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()

background_img = pygame.image.load("photo/galaxy (1).jpg")
background_img = pygame.transform.scale(background_img, [700, 500])
game = True

data = read_file()
#save_file(data)

hero = Player(7, 500, 400, 50, 50, data["skin"])

enemies = []
y =  50
for i in range(10):
    enemies.append(Enemy(3, random.randint(0, 600), y, 50, 50, "photo/ufo (1).png"))
    y -= 100

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  #
            print(pygame.mouse.get_pos())  #



    for bullet in hero.bullets[:]:
        for enemy in enemies:
            if bullet.hitbox.colliderect(enemy.hitbox):
                hero.bullets.remove(bullet)
                enemy.hitbox.y = -100
                enemy.hitbox.x = random.randint(0, 600)

                data= read_file()
                data["money"] += 1
                save_file(data)
                break


    hero.update()

    window.fill([123, 123,123 ])
    window.blit(background_img, [0,0])

    hero.draw(window)

    for enemy in enemies:
        enemy.draw(window)
        enemy.update()


    pygame.display.flip()

    clock.tick(60)