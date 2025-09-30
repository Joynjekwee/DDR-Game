def user(score, filename):
    import pygame
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen2 = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("User Input")

    base_font = pygame.font.Font(None, 40)
    # load the icon
    dance = pygame.image.load('dancer.png')
    # scale image down by half
    dance = pygame.transform.scale(dance, (int(dance.get_width() / 8), int(dance.get_height() / 8)))
    # get dimensions of scaled image
    dance_width, dance_height = dance.get_size()
    screen2.blit(dance, (screen_width - dance_width, screen_height - dance_height))
    pygame.display.update()


    name_disp = base_font.render("Please enter your name: ", True, (255, 255,255))
    screen2.blit(name_disp, (100,200))
    pygame.display.update()

    name = ''

    #box tfor input
    input_rect = pygame.Rect(450,200,250,40)
    clear_rect = pygame.Rect(450, 200, 250, 40) #x,y,width,height
    LIGHTBLUE = (173,216,230)

    #Colours
    WHITE = (255,255,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
                if event.key == pygame.K_RETURN:
                    with open(filename, 'a', newline='') as f: #opens file with append mode(add content to end of file)
                        f.write(f"{name.strip()}: {score}\n") #writes string to file
                    scores = []  # save scores

                    # read scores from file and append to the list
                    with open(filename, 'r') as f:
                        for line in f:
                            name, score_str = line.split(':')
                            score = int(score_str.strip())
                            scores.append((name.strip(), score))

                    scores.sort(key=lambda x: x[1], reverse=True)

                    with open(filename, 'w', newline='') as f:
                        for name, score in scores:
                            f.write(f"{name}: {score}\n")
                    name = ''  # clear the input string
                    input_rect.w = 250  # reset the input box width

                    pygame.quit()
                    return


        pygame.draw.rect(screen2,LIGHTBLUE,input_rect,2)
        pygame.draw.rect(screen2, LIGHTBLUE, clear_rect)

        text_surface = base_font.render(name,True,(0,0,0))
        screen2.blit(text_surface, (input_rect.x +5,input_rect.y+5))

        #input_rect.w = max(100,text_surface.get_width() + 10)

        pygame.display.update()
