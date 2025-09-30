import pygame
import librosa
import numpy as np
import scipy
import random






pygame.init()
pygame.mixer.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("DDR Rhythm Game")
font = pygame.font.Font(None, 36)
text = font.render("left arrow key: Leaderboard  right arrow key: Start  down arrow key: Quit", True, (255, 0, 0))
text2=font.render("Game Loading",True,(255,0,0))
text3=font.render("Leaderboard Loading",True,(255,0,0))
with open('gamemenupygame', 'r') as f:
   script_contents = f.read()


compiled_code=compile(script_contents,'gamemenupygame','exec')


with open('leaderboard','r') as f:
   leaderboard_contents=f.read()


leaderboard_compiled=compile(leaderboard_contents,'leaderboard','exec')


with open('loadingscreen','r') as f:
   loading_screen=f.read()


loading=compile(loading_screen,'loadingscreen','exec')


background_image = pygame.image.load('start_menu.png')

#
filename="Score_Sheet.txt"
return3=0
running = True
while running:


   screen.blit(background_image, (0, 0))
   pygame.display.update()
   clock.tick(60)


   for event in pygame.event.get():




       if event.type == pygame.QUIT:
           running = False






       elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:


           exec(loading)
           #exec(compiled_code)
           #for event in pygame.event.get():
            #  if event.type == pygame.KEYDOWN:
             #  if event.key == pygame.K_RIGHT:
           run = True
           while run:
               code_locals = {}
               exec(compiled_code, code_locals)
               return3=1
               if return3 == 1:
                   pygame.init()
                   screen = pygame.display.set_mode((screen_width, screen_height))
                   run = False








         if event.key == pygame.K_LEFT:
             #scores=Leaderboard.board(filename)
             #print(scores)
             exec(leaderboard_compiled)


             #event in pygame.event.get()
             #if event.type==pygame.KEYDOWN:
              #if event.key==pygame.K_RIGHT:
               #      screen.blit(text2,(60,400))
                #     pygame.display.flip()
                 #    screen = pygame.display.set_mode((screen_width, screen_height))
                  #   pygame.display.set_caption("DDR Rhythm Game")
                   #  continue


         if event.key==pygame.K_DOWN:
             running=False


   continue
pygame.display.update()
