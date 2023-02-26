import pygame, json


def draw_top_3():

    with open('score.json', 'r') as file:
        user_list = json.load(file)
    
    print(dict(sorted(user_list.items(), key=lambda x:x[1])))

    

draw_top_3()