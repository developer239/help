import pygame, sys
import math

pygame.init()

###########################################################################
###########################################################################

class Settings:
    resolutions = ["Low", "Normal", "High"]
    resolution = "Normal"

    window_sizes = ["Small", "Normal", "Big"]
    window_size = "Big"

    gameplay_options = ["Arrows/Space", "Mouse", "Mouse/Space", "WASD/Space", "WASD/Mouse"]
    gameplay = "Mouse"
sets = Settings()

###xxx###

# RESOLUTIONS

###xxx###

if sets.window_size not in sets.window_sizes:
    print("Invalid window size.")
elif sets.window_size == "Small":
    screen_width = 800
    screen_height = 400
    x = 1
    y = 1
    index1 = 0
elif sets.window_size == "Normal":
    screen_width = 1200
    screen_height = 600
    x = 1.5	
    y = 1.5
    index1 = 1
elif sets.window_size == "Big":
    screen_width = 1800
    screen_height = 900
    x = 2.25
    y = 2.25
    index1 = 2

screenxy = (screen_width, screen_height)

###########################################################################
###########################################################################

#GAME SETTINGS
screen = pygame.display.set_mode(screenxy)
pygame.display.set_caption("Meteor shooter - ZZ")


#IMAGES
ship = pygame.image.load("graphics/ship.png").convert_alpha()
background = pygame.image.load("graphics/background.png").convert()
START_butt = pygame.image.load("graphics/START.png").convert_alpha()
EXIT_butt = pygame.image.load("graphics/EXIT.png").convert_alpha()
SETTINGS_butt = pygame.image.load("graphics/SETTINGS.png").convert_alpha()
SETTINGS_butt_scale = pygame.transform.scale(SETTINGS_butt, (37*x,37*y))


#TEXT
font_size = 50
font0 = pygame.font.Font("graphics/subatomic.ttf", font_size)
font1 = pygame.font.Font("graphics/Oswald-Medium.ttf", font_size)
text0 = font0.render("Meteor shooter", True, "grey50")
gameplay_text0 = font1.render(f"Gameplay:  <-   {sets.gameplay}   -> ", True, "grey40")
window_size_text0 = font1.render(f"Window size:  <-   {sets.window_size}   -> ", True, "grey40")

#OBJECT SETTINGS
ship_rect = ship.get_rect(center = (screen_width/2, math.floor(screen_height/4*3.1)))
start_rect = START_butt.get_rect(center = (screen_width/2 - 200*x, screen_height/2 + 30*y))
exit_rect = EXIT_butt.get_rect(center = (screen_width/2 + 200*x, screen_height/2 + 30*y))
settings_rect = SETTINGS_butt.get_rect(center = (screen_width - 50*x, 10*y))


#OTHER
i = 1
MENU_BOUNCE = False
clock = pygame.time.Clock()
MENU = True
SETTINGS = False
move_up = False
move_down = False
move_left = False
move_right = False
index0 = 0

max_index0 = len(sets.gameplay_options) - 1
max_index1 = len(sets.window_sizes) - 1
settings_selected_any = False
settings_selected_index = 0

win_changed = False



def shoot():
    pass
#sizes
###########################################################################
###########################################################################



while True:
    
    #### events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            if start_rect.x <= mouse[0] <= start_rect.x + start_rect.width and start_rect.y <= mouse[1] <= start_rect.y + start_rect.height:
                MENU = False
            if exit_rect.x <= mouse[0] <= exit_rect.x + exit_rect.width and exit_rect.y <= mouse[1] <= exit_rect.y + exit_rect.height and MENU == True:
                pygame.quit()
                sys.exit()
            if settings_rect.x <= mouse[0] <= settings_rect.x + settings_rect.width and settings_rect.y <= mouse[1] <= settings_rect.y + settings_rect.height:
                SETTINGS = True
                MENU = False
            if SETTINGS == True and screen_width/2-gameplay_text0.get_width() <= mouse[0] <= screen_width/2+gameplay_text0.get_width() and screen_height/4 <= mouse[1] <= screen_height/4+gameplay_text0.get_height():
                index0 = index0 +1
                sets.gameplay = sets.gameplay_options[index0]
                gameplay_text0 = font1.render(f"Gameplay:  <-   {sets.gameplay}   -> ", True, "grey40")
            if SETTINGS == True and screen_width/2-window_size_text0.get_width() <= mouse[0] <= screen_width/2+window_size_text0.get_width() and screen_height/4*2 <= mouse[1] <= screen_height/4*2+window_size_text0.get_height():
                win_changed = True
                index1 = index1 +1
                sets.window_size = sets.window_sizes[index1]
                window_size_text0 = font1.render(f"Window size:  <-   {sets.window_size}   -> ", True, "grey40")
        
        if event.type == pygame.KEYDOWN and SETTINGS == True:
            if event.key == pygame.K_RETURN:
                if settings_selected_any == False:
                    settings_selected_any = True
                    settings_selected_index = settings_selected_index + 1
                    
                elif settings_selected_any == True:
                    settings_selected_any = False
                    settings_selected_index = 0

        if SETTINGS == False and settings_selected_any == True:
            settings_selected_any = False
            settings_selected_index = 0
        
        if event.type == pygame.KEYDOWN and SETTINGS == True and settings_selected_any == True:
            if event.key == pygame.K_DOWN:
                settings_selected_index = settings_selected_index + 1
            if event.key == pygame.K_UP:
                settings_selected_index = settings_selected_index - 1
            if settings_selected_index > 1:
                settings_selected_index = 1
            if settings_selected_index < 0:
                settings_selected_index = 0
            if event.key == pygame.K_LEFT:
                if settings_selected_index == 0:
                    index0 = index0 - 1
                    sets.gameplay = sets.gameplay_options[index0]
                    gameplay_text0 = font1.render(f"Gameplay:  <-   {sets.gameplay}   -> ", True, "grey40")
                if settings_selected_index == 1:
                    index1 = index1 - 1
                    sets.window_size = sets.window_sizes[index1]
                    window_size_text0 = font1.render(f"Window size:  <-   {sets.window_size}   -> ", True, "grey40")
            if event.key == pygame.K_RIGHT:
                if settings_selected_index == 0:
                    index0 = index0 + 1
                    sets.gameplay = sets.gameplay_options[index0]
                    gameplay_text0 = font1.render(f"Gameplay:  <-   {sets.gameplay}   -> ", True, "grey40")
                if settings_selected_index == 1:
                    index1 = index1 + 1
                    sets.window_size = sets.window_sizes[index1]
                    window_size_text0 = font1.render(f"Window size:  <-   {sets.window_size}   -> ", True, "grey40")
                    

        if index0 == max_index0:
            index0 = 0
        if index1 == max_index1:
            index1 = -1
        
        if event.type == pygame.MOUSEMOTION and MENU == False and SETTINGS == False and Settings.gameplay == "Mouse":
            ship_rect.center = event.pos
            
        if event.type == pygame.KEYDOWN and MENU == False:
            if event.key == pygame.K_ESCAPE:
                SETTINGS = True
            if SETTINGS == True and event.key == pygame.K_ESCAPE:
                SETTINGS = False
            if event.key == pygame.K_UP:
                move_up = True    
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_r:
                MENU = True
                SETTINGS = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
                    
    if move_up == True:
        ship_rect.y -= 10
    if move_down == True:
        ship_rect.y += 10
    if move_left == True:
        ship_rect.x -= 10
    if move_right == True:
        ship_rect.x += 10

    if sets.gameplay not in sets.gameplay_options:
        print("Invalid gameplay option.")
    elif sets.gameplay == "Arrows/Space":
        shoot = pygame.K_SPACE
        move_up = pygame.K_UP
        move_down = pygame.K_DOWN
        move_left = pygame.K_LEFT
        move_right = pygame.K_RIGHT
    elif sets.gameplay == "Mouse":
        pass
        shoot()





    #### 
    screen.fill("grey13")
    clock.tick(80)
    #### 
    # updates
    mouse = pygame.mouse.get_pos()

    # surfaces(blit and location)
    screen.blit(background, (0, 0))
    screen.blit(SETTINGS_butt_scale, (screen_width - SETTINGS_butt.get_width()+30*x, 20))
    
    #/#screen.blit(ship, (i, ship_rect.y + ship.get_height()/2))
    
    # MAIN SCREEN SHIP MOVEMENT
    if MENU == True:
        screen.blit(ship, (i, ship_rect.y + ship.get_height()/2))
        if i >= screen.get_width() - ship.get_width():
            MENU_BOUNCE = True
        elif i <= 0:
            MENU_BOUNCE = False
            
        if MENU_BOUNCE == True:
            i = i - 3*x
        else: i = i + 3*x

        #MAIN SCREEN TEXT
        screen.blit(text0, (screen_width/2 - text0.get_width()/2, screen_height/2-(30*y) - text0.get_height()/2))
        #MAIN SCREEN BUTTONS
        screen.blit(START_butt, start_rect)
        screen.blit(EXIT_butt, exit_rect)
    if MENU == False and SETTINGS == False:
        screen.blit(ship, ship_rect)
    if SETTINGS == True:
        screen.blit(gameplay_text0, (screen_width/3, screen_height/4))
        if settings_selected_index == 0 and settings_selected_any == True:
            pygame.draw.rect(screen, "grey", gameplay_text0.get_rect(topleft = (screen_width/3-5*x, screen_height/4)), 3)
        if settings_selected_index == 1 and settings_selected_any == True:
            pygame.draw.rect(screen, "grey", window_size_text0.get_rect(topleft = (screen_width/3-5*x, screen_height/4*2)), 3)
        
        screen.blit(window_size_text0, (screen_width/3, screen_height/4*2))
        if index1 == 0:
            if win_changed:
                #screenxy = (800, 400)
                #screen = pygame.display.set_mode(screenxy)
                win_changed = False
        if index1 == 1:
            if win_changed:
                screenxy = (1200, 600)
                x = 1.5
                y = 1.5
                screen = pygame.display.set_mode(screenxy)
                win_changed = False
        if index1 == -1:
            if win_changed:
                screenxy = (1800, 900)
                x = 2.25
                y = 2.25
                screen = pygame.display.set_mode(screenxy)
                win_changed = False
        if win_changed:
            print(index1)
           



        
    ### SETTINGS

    
        

               
#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#
        

    pygame.display.update()