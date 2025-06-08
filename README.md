import pygame

import random

pygame.init()


window = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()


background_img = pygame.image.load("photo/galaxy (1).jpg")


class Rocket():
    def __init__(self, x, y, texture, speed, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.hitbox.left > 0:
            self.hitbox.x -= self.speed
        if keys[pygame.K_RIGHT] and self.hitbox.right < 800:
            self.hitbox.x += self.speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

class Enemy():
    def __init__(self, x, y, texture, speed, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def move(self):
        self.hitbox.y += self.speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)


rocket = Rocket(350, 500, "photo/rocket (1).png", speed=5, w=80, h=100)


enemies = []


SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == SPAWN_EVENT:
            x = random.randint(0, 730)
            enemy = Enemy(x, 0, "photo/ufo (1).png", speed=2, w=70, h=70)
            enemies.append(enemy)


    rocket.move()


    window.blit(background_img, (0, 0))


    for enemy in enemies:
        enemy.move()
        enemy.draw(window)


        if rocket.hitbox.colliderect(enemy.hitbox):
            enemies.remove(enemy)


    rocket.draw(window)

    pygame.display.flip()
    clock.tick(60)
