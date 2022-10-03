import pygame, sys

class StartScreen:

    # initializing the constructor for pygame
    pygame.init() 
    
    screen_resolution = (800, 600) 
    screen_window = pygame.display.set_mode((screen_resolution))
    font_color = (0, 0, 0)
    start_button_color = (192, 192, 192) 
    hover_start_button_color = (255,255,255)
    background_color = (79, 121, 66)
    screen_width = screen_window.get_width() 
    screen_height = screen_window.get_height()
    fonts = pygame.font.get_fonts()
    
    start_button_font = pygame.font.SysFont('impact',30) 
    
    # creating text for the quit button
    text = start_button_font.render('Quit' , True , font_color) 
    
    while True: 
        
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if screen_width/2 <= mouse[0] <= screen_width/2+140 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
                    pygame.quit() 
                    
        # fills the screen with a color 
        screen_window.fill(background_color) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if screen_width/2 <= mouse[0] <= screen_width/2+140 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
            pygame.draw.rect(screen_window,start_button_color,[screen_width/2,screen_height/2,140,40]) 
            
        else: 
            pygame.draw.rect(screen_window,hover_start_button_color,[screen_width/2,screen_height/2,140,40]) 
        
        # superimposing the text onto our button 
        screen_window.blit(text , (screen_width/2+50,screen_height/2)) 
        
        # updates the frames of the game 
        pygame.display.update() 