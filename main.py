import pygame, sys, json
from style import *
from snake import main as snake
from button import BUTTON

# Functions 

def get_font(size):
    return pygame.font.Font("assets/GLS.ttf", size)

def write_text(text, size, x, y):
    text_font = get_font(size)
    title_surface = text_font.render(text, True, BLACK, PURPLE)
    score_rect = title_surface.get_rect(center = (x, y))
    screen.blit(title_surface, score_rect)


# menu Function 

def def_user():
    #PYGAME
    pygame.init()
    word=""
    # window parameter
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color(PURPLE))

    write_text("Enter your username: ", 60, 300, 100) #example asking name
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    word += event.unicode.upper()
                
                if event.key == pygame.K_RETURN:
                    return word
                    

        # timer and FPS
        pygame.display.update()
        clock.tick(60)

        write_text(word, 40, 300, 300) 

menu_button = BUTTON(WHITE, 200 ,500, 200, 60, "Back")

def scoreboard():
    #PYGAME
    pygame.init()
    # window parameter
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color(PURPLE))

    write_text("Scoreboard", 60, 300, 100) #example asking name
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.is_over(pygame.mouse.get_pos()):
                    main()

        draw_top_3()

        # timer and FPS
        pygame.display.update()
        clock.tick(60)
        menu_button.draw(screen)


def draw_top_3():

    with open('score.json', 'r') as file:
        user_list = json.load(file)
    
    sorted_user_list = dict(sorted(user_list.items(), key=lambda x:x[1]))
    first_three_items = list(sorted_user_list.items())[-3:]

    write_text(first_three_items[2][0] + " : " + str(first_three_items[2][1]), 30, 300, 200)
    write_text(first_three_items[1][0] + " : " + str(first_three_items[1][1]), 30, 300, 300)
    write_text(first_three_items[0][0] + " : " + str(first_three_items[0][1]), 30, 300, 400)

#PYGAME
pygame.init()

# window parameter
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# clock parameter
clock = pygame.time.Clock() #clock normalize speed of exe in every computer(not impacted anymore by it calculation speed)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #150 ms 

#My buttons         (color, x, y, width, height, text):

play_button = BUTTON(WHITE, 200 ,200, 200, 60, "Play")
scoreboard_button = BUTTON(WHITE, 150, 300, 300, 60, "Scoreboard")
exit_button = BUTTON(WHITE, 200 ,400, 200, 60, "Exit")


#Main loop

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.is_over(pygame.mouse.get_pos()):
                        username = def_user()
                        snake(username) 
                    if scoreboard_button.is_over(pygame.mouse.get_pos()):
                        scoreboard()
                    if exit_button.is_over(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

        # display elements

        screen.fill(pygame.Color(PURPLE))

        write_text("Snake Game", 72, 300, 100)
        # Draw buttons 
            
        play_button.draw(screen)
        scoreboard_button.draw(screen)
        exit_button.draw(screen)

        # timer and FPS
        pygame.display.update()
        clock.tick(60)

main()