 import pygame

             pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Leaderboard")
screen.fill((0,0,0)) #change colour of screen

#load the icon
dance = pygame.image.load('dancer.png')
#scale image down by half
dance = pygame.transform.scale(dance, (int(dance.get_width()/8), int(dance.get_height()/8)))
#get dimensions of scaled image
dance_width, dance_height = dance.get_size()
screen.blit(dance, (screen_width-dance_width,screen_height-dance_height))
pygame.display.update()

# font for header and leaderboard rows
header_font = pygame.font.Font(None, 40)
font = pygame.font.Font(None, 30)

# Define colours
YELLOW = (255,255,0)
WHITE = (255, 255, 255)
LIGHTBLUE = (173,216,230)

# Headings
title = header_font.render("HIGH  SCORES", True, LIGHTBLUE)
rank_heading = header_font.render("RANK", True, YELLOW)
name_heading = header_font.render("NAME", True, YELLOW)
score_heading = header_font.render("SCORE", True, YELLOW)

#Add headings to screen
title_pos = (screen_width - title.get_rect().width)// 2
rank_heading_pos = (110,80)
name_heading_pos = (350, 80)
score_heading_pos = (600, 80)
screen.blit(title, (title_pos, 30))
screen.blit(rank_heading,rank_heading_pos)
screen.blit(name_heading,name_heading_pos)
screen.blit(score_heading,score_heading_pos)

# Load the scores from the file
filename = "Score_Sheet.txt"
scores = []
with open(filename, 'r') as f:
    for line in f:
        name, score_str = line.strip().split(': ')
        score = int(score_str)
        scores.append((name, score))

# Sort the scores in descending order
scores.sort(key=lambda x: x[1], reverse=True)

# Take the top 10 scores and names

# Draw the leaderboard on the screen
y = 130
for i, (name, score) in enumerate(scores[:10], 1):
    rank = font.render(str(i), True, LIGHTBLUE)
    name = font.render(name, True, WHITE)
    score1 = font.render(str(score), True, WHITE)
    screen.blit(rank, (150, y))
    screen.blit(name, (350, y))
    screen.blit(score1, (600, y))
    y += 30

# Update the display
pygame.display.update()

run = True
# Wait for the user to quit the game
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
              run=False
