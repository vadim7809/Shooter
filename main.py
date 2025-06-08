import pygame
import sys
import random  # імпорт для рандому

pygame.init()

# Вікно
window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Rocket vs Enemies")
clock = pygame.time.Clock()

# Фон
background_img = pygame.image.load("photo/backgr.png")

# Клас ракети
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

# Клас ворога
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

# Ракета
rocket = Rocket(350, 500, "photo/rocket.png", speed=5, w=80, h=100)

# Список ворогів
enemies = []

# Таймер появи ворога (мілісекунди)
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1000)  # кожну 1 секунду

# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Додаємо ворога
        if event.type == SPAWN_EVENT:
            x = random.randint(0, 730)  # Випадкове X (ширина екрану - ворог ~70px)
            enemy = Enemy(x, 0, "photo/enemy1.png", speed=2, w=70, h=70)
            enemies.append(enemy)

    # Рух ракети
    rocket.move()

    # Фон
    window.blit(background_img, (0, 0))

    # Вороги
    for enemy in enemies[:]:  # копія списку
        enemy.move()
        enemy.draw(window)

        # Зіткнення
        if rocket.hitbox.colliderect(enemy.hitbox):
            enemies.remove(enemy)

    # Ракета
    rocket.draw(window)

    pygame.display.flip()
    clock.tick(60)
