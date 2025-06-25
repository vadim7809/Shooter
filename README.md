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
def start_game():
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


ДЖСССССС


import json



def read_file():
    try:
        with open("data.json" ,"r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except:
        return {
            "skin": "rocket (1).png",
            "money": 0
        }

def save_file(data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data,file, ensure_ascii=False)





2





import random

import pygame
from shop import*
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
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(10,self.hitbox.x+10,self.hitbox.y,10,20,("bullet (1).png")))

        for bullet in self.bullets:
            bullet.upgrade()
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
    def upgrade(self):
        self.hitbox.y -= self.speed


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
    def upgrade(self):
        global missed_enemy
        self.hitbox.y += self.speed
        if self.hitbox.y >500:
            self.hitbox.y =-100
            self.hitbox.x = random.randint(0,600)
            missed_enemy += 1
def start_game():

    pygame.init()
    window = pygame.display.set_mode([700, 500])
    clock = pygame.time.Clock()

    background_img = pygame.image.load("photo/galaxy (1).jpg")
    background_img = pygame.transform.scale(background_img, [700, 500])
    game = True

    data = read_file()


    hero = Player(10, 500, 400, 50, 50, data["skin"])

    enemies = []
    y =  50
    for i in range(10):
        enemies.append(Enemy(5, random.randint(0, 600), y, 50, 50, "ufo (1).png"))
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
                    enemy.hitbox.x = random.randint(0,600)

                    data = read_file()
                    data["money"] += 1
                    save_file(data)
                    break





        hero.update()
        window.fill([123, 123,123 ])
        window.blit(background_img, [0,0])

        hero.draw(window)

        for enemy in enemies:
            enemy.draw(window)
            enemy.upgrade()

        pygame.display.flip()

        clock.tick(60)





ШОП








from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from file_helper import *
from main import *
def buy_item(price, img):
    data = read_file()
    if data["money"] >= price:
        data["skin"] = img
        data["money"] -= price
        save_file(data)
    else:
        print("Немає грошей")
def shop_window():
    window = QDialog()

    elements = [
        {
            "name": "test1",
            "img":  "rocket.png",
            "price": 100

        }
    ]

    main_line = QHBoxLayout()
    for element in elements:
        ver = QVBoxLayout()
        name_lbl = QLabel(element["name"])
        img_lbl = QLabel()
        img_pm = QPixmap(element["img"])
        img_pm = img_pm.scaledToWidth(100)
        img_lbl.setPixmap(img_pm)
        price_lbl = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")
        buy_btn.clicked.connect(lambda _,
                                       price=element["price"],
                                       img=element["img"] : buy_item(price, img))
        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)
        main_line.addLayout(ver)




    window.setLayout(main_line)
    window.show()
    window.exec()







МЕНЮ


from PyQt6.QtWidgets import *
from main import *
from shop import *

app = QApplication([])
window = QWidget()
stat_btn = QPushButton("Почати")
shop_btn = QPushButton("Магазин")
exit_btn = QPushButton("Вийти")

main_line = QVBoxLayout()
main_line.addWidget(stat_btn)
main_line.addWidget(shop_btn)
main_line.addWidget(exit_btn)

window.setLayout(main_line)

stat_btn.clicked.connect(start_game)
shop_btn.clicked.connect(shop_window)


window.show()
app.exec()