import pygame, sys, random
from style import *
from pygame.math import Vector2 #Allow me to simply call Vector2

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen, dark_purple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, light_purple, block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] #delete the last element off the body

        body_copy.insert(0, body_copy[0] + self.direction) #make the head move forward to make the snake move
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()  
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            # reposition fruit
            self.fruit.randomize()
            # add a block to the snake
            self.snake.add_block()

pygame.init()
#define my grind dependinc on cell number to make it easily modulable
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock() #clock normalize speed of exe in every computer(not impacted anymore by it calculation speed)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #150 ms 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1) #change vector to go up
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0) 
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1) 
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0) 
                
    screen.fill(pygame.Color(light_blue))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)