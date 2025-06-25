import pygame
import random
from file_helper import read_file, save_file

class Player:
    def __init__(self, speed, x, y, width, height, skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, (width, height))
        self.hitbox = self.skin.get_rect(topleft=(x, y))
        self.bullets = []
        self.shoot_cooldown = 0

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

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if keys[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.bullets.append(Bullet(10, self.hitbox.centerx - 5, self.hitbox.y, 10, 20, "bullet (1).png"))
            self.shoot_cooldown = 15

        for bullet in self.bullets[:]:
            bullet.upgrade()
            if bullet.hitbox.y < -20:
                self.bullets.remove(bullet)

class Bullet:
    def __init__(self, speed, x, y, width, height, skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, (width, height))
        self.hitbox = self.skin.get_rect(topleft=(x, y))

    def draw(self, window):
        window.blit(self.skin, self.hitbox)

    def upgrade(self):
        self.hitbox.y -= self.speed

class Enemy:
    def __init__(self, speed, x, y, width, height, skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, (width, height))
        self.hitbox = self.skin.get_rect(topleft=(x, y))

    def draw(self, window):
        window.blit(self.skin, self.hitbox)

    def upgrade(self):
        self.hitbox.y += self.speed
        if self.hitbox.y > 500:
            self.hitbox.y = -100
            self.hitbox.x = random.randint(0, 600)
            return True
        return False

def draw_text(window, text, size, x, y, color=(255,255,255)):
    font = pygame.font.SysFont("arial", size)
    render = font.render(text, True, color)
    window.blit(render, (x, y))

def start_game():
    pygame.init()
    window = pygame.display.set_mode([700, 500])
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    background_img = pygame.image.load("galaxy (1).jpg")
    background_img = pygame.transform.scale(background_img, [700, 500])

    data = read_file()
    hero = Player(10, 500, 400, 50, 50, data["skin"])
    enemies = [Enemy(2, random.randint(0, 600), -i * 100, 50, 50, "ufo (1).png") for i in range(10)]

    missed_enemy = 0
    killed_enemy = 0
    game = True
    game_over = False
    victory = False

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if not game_over and not victory:
            for bullet in hero.bullets[:]:
                for enemy in enemies:
                    if bullet.hitbox.colliderect(enemy.hitbox):
                        hero.bullets.remove(bullet)
                        enemy.hitbox.y = -100
                        enemy.hitbox.x = random.randint(0, 600)
                        data["money"] += 1
                        killed_enemy += 1
                        save_file(data)
                        break

            hero.update()

            for enemy in enemies:
                if enemy.upgrade():
                    missed_enemy += 1

            if missed_enemy >= 10:
                game_over = True
            if killed_enemy >= 20:
                victory = True

        window.blit(background_img, (0, 0))
        hero.draw(window)
        for enemy in enemies:
            enemy.draw(window)

        draw_text(window, f" {data['money']}", 30, 10, 10)
        draw_text(window, f" {missed_enemy}", 30, 10, 50)
        draw_text(window, f" {killed_enemy}", 30, 10, 90)

        if game_over:
            draw_text(window, "GAME OVER", 60, 250, 200, (255, 0, 0))
        if victory:
            draw_text(window, "YOU WIN!", 60, 250, 200, (0, 255, 0))

        pygame.display.flip()
        clock.tick(60)
