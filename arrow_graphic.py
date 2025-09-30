# Setting up the window
import pygame, sys, math
from pygame.locals import *

#Set up pygame
pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

#background_image = pygame.image.load('background_1.jpg')
#background_image = pygame.transform.scale(background_image, (800, 600))

pygame.display.set_caption('Pygame Rhythm Game')

# Load in the Left Arrow
larrow = pygame.image.load('left_arrow_outline.png')

new_width = 200
new_height = 200

resized_larrow = pygame.transform.scale(larrow, (new_width, new_height))

#Load in the right arrow
rarrow = pygame.image.load('right_arrow_outline.png')

resized_rarrow = pygame.transform.scale(rarrow, (new_width, new_height))

#Load in the down arrow
darrow = pygame.image.load('dowm_arrow_outline.png')

resized_darrow = pygame.transform.scale(darrow, (new_width, new_height))

#Load in the up arrow
uarrow = pygame.image.load('up_arrow_outline.png')

resized_uarrow = pygame.transform.scale(uarrow, (new_width, new_height))

#Assigning each of the arros a specific coordinate (left, right, up, down)
image1 = pygame.transform.scale(pygame.image.load('left_arrow.png'), (new_width, new_height))
image2 = pygame.transform.scale(pygame.image.load('right_arrow.png'), (new_width, new_height))
image3 = pygame.transform.scale(pygame.image.load('up_arrow.png'), (new_width, new_height))
image4 = pygame.transform.scale(pygame.image.load('down_arrow.png'), (new_width, new_height))

image1_rect = image1.get_rect()
image1_rect.x = 0
image1_rect.y = 0
velocity = [2, 2]

image2_rect = image2.get_rect()
image2_rect.x = 0
image2_rect.y = 0
velocity = [2, 2]

image3_rect = image3.get_rect()
image3_rect.x = 0
image3_rect.y = 0
velocity = [2, 2]

image4_rect = image4.get_rect()
image4_rect.x = 0
image4_rect.y = 0
velocity = [2, 2]

#left arrow image
coordinates = [
    (100, 0),
    (100, 100),
    (100, 200),
    (100, 300),
    (100, 400),
    (100, 500),
    (100, 600),
]
current_coordinate_index1 = 0

#right arrow image
coordinates = [
    (250, 0),
    (250, 100),
    (250, 200),
    (250, 300),
    (250, 400),
    (250, 500),
    (250, 600),
]
#up arrow image
#down arrow image




#Load in the arrows for the game





#Game Loop; keeps the pygame window open until user quits.
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.blit(background_image, (0, 0))
    screen.fill((0, 0, 0))

    screen.blit(image1, image1_rect)
    screen.blit(image2, image2_rect)
    screen.blit(image3, image3_rect)
    screen.blit(image4, image4_rect)

    screen.blit(resized_larrow, (100, 450))
    screen.blit(resized_rarrow, (250, 450))
    screen.blit(resized_uarrow, (400, 450))
    screen.blit(resized_darrow, (550, 450))

    pygame.display.flip()
    pygame.display.update()

    target_x, target_y = coordinates[current_coordinate_index1]
    dx, dy = target_x - image1_rect.x, target_y - image1_rect.y



    if abs(dx) < 1 and abs(dy) < 1:
        current_coordinate_index1 = (current_coordinate_index1 + 1) % len(coordinates)
    else:
        angle = math.atan2(dy, dx)
        image1_rect.x += velocity[0] * math.cos(angle)
        image1_rect.y += velocity[1] * math.sin(angle)

    clock.tick(120)

pygame.quit()