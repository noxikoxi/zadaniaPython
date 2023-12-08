import datetime
import random
import sys

import pygame
from pygame import Vector2

BLOCK_WIDTH = 60
N_BLOCKS = 11
WINDOWS_HEIGHT, WINDOWS_WIDTH = BLOCK_WIDTH * N_BLOCKS, BLOCK_WIDTH * N_BLOCKS
GAME_SPEED = 180
FPS = 60

pygame.init()
pygame.font.init()
pygame.display.set_caption("Snake")
pygame.key.set_repeat(0)

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, GAME_SPEED)

GRID_COLORS = ((180, 180, 180), (140, 90, 90))


class Fruit:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.randomize()
        self.color = 'red'

        self.updateNum = 20  # Po 10 Update zniknie

    def resetUpdateNum(self):
        self.updateNum = 20

    def randomize(self):
        self.x = random.randint(0, N_BLOCKS - 1)
        self.y = random.randint(0, N_BLOCKS - 1)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, ((self.x+0.5) * BLOCK_WIDTH,
                                                (self.y+0.5) * BLOCK_WIDTH), radius=BLOCK_WIDTH/2)


class RottenFruit(Fruit):
    def __init__(self):
        super().__init__()
        self.color = (10, 10, 10)


class Snake:
    def __init__(self):
        self.direction = None
        self.body = None
        self.reset()
        self.add_block = False
        self.remove_block = False

        self.bodyColor = (0, 255, 0)
        self.headColor = (0, 200, 50)

    def move(self):
        if self.add_block:
            self.body.insert(0, self.body[0] + self.direction)
            self.add_block = False
        elif self.remove_block:
            self.body = self.body[:-1]
            if len(self.body) == 0:
                self.reset()
            self.remove_block = False
        elif self.direction != Vector2(0, 0):
            if len(self.body) > 1:
                self.body = self.body[:-1]
                self.body.insert(0, self.body[0] + self.direction)
            else:
                self.body[0] += self.direction

        if self.body[0].x >= N_BLOCKS:
            self.body[0].x = 0
        elif self.body[0].x <= -1:
            self.body[0].x = N_BLOCKS
        elif self.body[0].y >= N_BLOCKS:
            self.body[0].y = 0
        elif self.body[0].y <= -1:
            self.body[0].y = N_BLOCKS

    def reset(self):
        self.body = [Vector2(N_BLOCKS // 2 + 1, N_BLOCKS // 2), Vector2(N_BLOCKS // 2, N_BLOCKS // 2),
                     Vector2(N_BLOCKS // 2 - 1, N_BLOCKS // 2)]
        self.direction = Vector2(0, 0)

    def draw(self, screen):
        # Head
        x, y = self.body[0]
        pygame.draw.rect(screen, self.headColor, pygame.rect.Rect(
            x * BLOCK_WIDTH + 1, y * BLOCK_WIDTH + 1, BLOCK_WIDTH - 2, BLOCK_WIDTH - 2
        ))

        # Body
        for block in self.body[1:]:
            pygame.draw.rect(screen, self.bodyColor, pygame.rect.Rect(
                block.x * BLOCK_WIDTH + 1, block.y * BLOCK_WIDTH + 1, BLOCK_WIDTH - 2, BLOCK_WIDTH - 2
            ))


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        self.rottenFruit = RottenFruit()
        self.font = pygame.font.Font(None, 60)
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.game_time = 3 * 60 # W sekundach

    def get_time_left(self):
        time_seconds = (pygame.time.get_ticks() - self.start_time) // 1000
        return datetime.timedelta(seconds=self.game_time) - datetime.timedelta(seconds=time_seconds)

    def draw(self):
        # Background
        self.screen.fill((0, 0, 0))
        for row in range(N_BLOCKS):
            for col in range(N_BLOCKS):
                if (row + col) % 2 == 0:
                    color = GRID_COLORS[0]
                else:
                    color = GRID_COLORS[1]

                pygame.draw.rect(self.screen, color, pygame.Rect(
                    col * BLOCK_WIDTH, row * BLOCK_WIDTH, BLOCK_WIDTH, BLOCK_WIDTH
                ))

        # Snake
        self.snake.draw(self.screen)

        # Fruit
        self.fruit.draw(self.screen)

        # RottenFruit
        self.rottenFruit.draw(self.screen)

        # Score
        text_surface = self.font.render(f'Score: {self.score}', True, 'yellow')
        self.screen.blit(text_surface, (BLOCK_WIDTH/3, BLOCK_WIDTH/4))

        # Time
        time_surface = self.font.render(str(self.get_time_left())[2:], True, 'yellow')
        self.screen.blit(time_surface, ((N_BLOCKS-3) * BLOCK_WIDTH, BLOCK_WIDTH/4))

    def checkCollisions(self):
        if Vector2(self.fruit.x, self.fruit.y) == self.snake.body[0]:
            self.snake.add_block = True
            self.spawnFruit(self.fruit, self.rottenFruit)
            self.score += 1

        if Vector2(self.rottenFruit.x, self.rottenFruit.y) == self.snake.body[0]:
            self.snake.remove_block = True
            self.spawnFruit(self.rottenFruit, self.fruit)
            self.score -= 1

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        print(f'Twoj koncowy wynik: {self.score}')
        self.score = 0
        self.start_time = pygame.time.get_ticks()

    def spawnFruit(self, fruit, otherFruit):
        fruit.randomize()
        while Vector2(fruit.x, fruit.y) in self.snake.body or Vector2(fruit.x, fruit.y) == Vector2(otherFruit.x, otherFruit.y):
            fruit.randomize()
        fruit.resetUpdateNum()

    def run(self):
        self.snake.move()
        self.checkCollisions()

        # Czas liczy sie dopiero po 1 ruchu
        if self.snake.direction == Vector2(0, 0):
            self.start_time = pygame.time.get_ticks()

        if self.get_time_left() == datetime.timedelta(seconds=0):
            self.game_over()

        self.fruit.updateNum -= 1
        self.rottenFruit.updateNum -= 1

        if self.fruit.updateNum <= 0:
            self.spawnFruit(self.fruit, self.rottenFruit)

        if self.rottenFruit.updateNum <= 0:
            self.spawnFruit(self.rottenFruit, self.fruit)


if __name__ == "__main__":
    main_game = Game()
    while True:
        changed_dir = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                pygame.font.quit()
                sys.exit()

            if event.type == UPDATE:
                main_game.run()

            if event.type == pygame.KEYDOWN:
                if not changed_dir:  # Unika sytuacji w której mozna szybko nacisnąc 2 klawisze
                    changed_dir = True
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y != 1:
                            main_game.snake.direction = Vector2(0, -1)
                    elif event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y != -1:
                            main_game.snake.direction = Vector2(0, 1)
                    elif event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x != -1:
                            main_game.snake.direction = Vector2(1, 0)
                    elif event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x != 1 and main_game.snake.direction != Vector2(0, 0):
                            main_game.snake.direction = Vector2(-1, 0)

        main_game.draw()
        pygame.display.update()
        main_game.clock.tick(FPS)
