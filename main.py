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
        # add a part to avoid fruit spawning on the snake body
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
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
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]: #head of snake  
            # reposition fruit
            self.fruit.randomize()
            # add a block to the snake
            self.snake.add_block()

    def check_fail(self):   
        #check if the snake hit the border
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        #check if the snake hit his self
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
            pygame.quit()
            sys.exit()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, deep_gray)
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)

pygame.init()
#define my grind dependinc on cell number to make it easily modulable
cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock() #clock normalize speed of exe in every computer(not impacted anymore by it calculation speed)
game_font = pygame.font.Font("Assets/Goodnight-London-Sans.ttf", 32)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #150 ms 

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1: #avoid to half turn
                    main_game.snake.direction = Vector2(0, -1) #change vector to go up
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0) 
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1) 
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:    
                    main_game.snake.direction = Vector2(-1, 0) 
                
    screen.fill(pygame.Color(light_blue))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)