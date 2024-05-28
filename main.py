import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Цвета
SKY_COLOR = (135, 206, 235)
GROUND_COLOR = (34, 139, 34)

# Кадров в секунду
FPS = 60
moving_left = False

# Установка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Моя игра в Pygame")

# Время
clock = pygame.time.Clock()

# Загрузка изображений
hero_img = pygame.image.load('graphics/hero.png').convert_alpha()
enemy_img = pygame.image.load('graphics/enemy.png').convert_alpha()

# Позиции героя и врага
hero_x, hero_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT - hero_img.get_height() - 30
enemy_x, enemy_y = 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - enemy_img.get_height() - 30
# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Клавиша 'A' была нажата!")
                moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("Клавиша 'A' была отпущена!")
                moving_left = False

    if moving_left == True:
        hero_x -= 1
    # Заливка фона цветом неба
    screen.fill(SKY_COLOR)

    # Рисование земли
    pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - 30, SCREEN_WIDTH, 30))

    # Рисование героя и врага
    screen.blit(hero_img, (hero_x, hero_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Обновление экрана
    pygame.display.flip()
    # Верхняя граница обновления, чтобы обновлялось не слишком часто
    clock.tick(FPS)

# Выход из Pygame
pygame.quit()
sys.exit()
