import random
import pygame
from file_helper import *
from PyQt6.QtWidgets import *

from shop import shop_window


class Bullet:
    def __init__(self, speed, x, y, width, height, skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.skin, self.hitbox)

    def update(self):
        self.hitbox.y -= self.speed

class Player:
    def __init__(self, speed, x, y, width, height, skin):
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
            self.bullets.append(
                Bullet(10, self.hitbox.x + 10, self.hitbox.y, 10, 20, "bullet (1).png")
            )
            shoot_sound = pygame.mixer.Sound("sounds/fire (1).ogg")



        for bullet in self.bullets:
            bullet.update()

class Enemy:
    def __init__(self, speed, x, y, width, height, skin):
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



def start_game():
    pygame.init()
    window = pygame.display.set_mode([700, 500])
    clock = pygame.time.Clock()

    background_img = pygame.image.load("galaxy (1).jpg")
    background_img = pygame.transform.scale(background_img, [700, 500])

    data = read_file()

    hero = Player(7, 500, 400, 50, 50, data["skin"])

    enemies = []
    y = 50
    for i in range(10):
        enemies.append(Enemy(2, random.randint(0, 600), y, 50, 50, "ufo (1).png"))
        y -= 100

    missed_enemy = 0
    killed_enemy = 0

    font = pygame.font.Font(None, 24)
    keys = pygame.key.get_pressed()

    pygame.mixer.init()
    pygame.mixer.music.load("sounds/space (1).ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for bullet in hero.bullets[:]:
            for enemy in enemies:
                if bullet.hitbox.colliderect(enemy.hitbox):
                    hero.bullets.remove(bullet)
                    enemy.hitbox.y = -100
                    enemy.hitbox.x = random.randint(0, 600)
                    data = read_file()
                    data["money"] += 1
                    save_file(data)
                    killed_enemy += 1
                    break

        hero.update()
        for enemy in enemies:
            enemy.hitbox.y += enemy.speed
            if enemy.hitbox.y > 500:
                enemy.hitbox.y = -100
                enemy.hitbox.x = random.randint(0, 600)
                missed_enemy += 1

        if killed_enemy >= 500:
            running = False


        window.fill([123, 123, 123])
        window.blit(background_img, [0, 0])




        money_text = font.render("Монет: " + str(data["money"]), True, (255, 255, 255))
        missed_text = font.render("Втікло: " + str(missed_enemy), True, (255, 255, 255))
        killed_text = font.render("Знищено: " + str(killed_enemy), True, (255, 255, 255))
        
        window.blit(money_text, (10, 10))
        window.blit(missed_text, (10, 40))
        window.blit(killed_text, (10, 70))

        hero.draw(window)

        for enemy in enemies:
            enemy.draw(window)
            enemy.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# --- Меню PyQt ---

def main_menu():
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("Головне меню")

    start_btn = QPushButton("Почати гру")
    shop_btn = QPushButton("Магазин")
    exit_btn = QPushButton("Вийти")

    layout = QVBoxLayout()
    layout.addWidget(start_btn)
    layout.addWidget(shop_btn)
    layout.addWidget(exit_btn)
    window.setLayout(layout)

    def on_start():
        window.hide()
        start_game()
        window.show()

    def shop():
        window.hide()
        shop_window()
        window.show()

    def on_exit():
        app.quit()



    start_btn.clicked.connect(on_start)
    shop_btn.clicked.connect(shop)
    exit_btn.clicked.connect(on_exit)

    window.show()
    app.exec()




