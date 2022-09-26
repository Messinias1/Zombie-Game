import pygame, sys

class StartScreen:

    # initializing the constructor 
    pygame.init() 
    
    # screen resolution 
    resolution = (1080,1080) 
    
    # opens up a window 
    screen = pygame.display.set_mode((800, 600))
    
    # white color 
    font_color = (0, 0, 0)
    
    # light shade of the button 
    start_button_color = (192, 192, 192) 
    
    # dark shade of the button while hovering over it with cursor
    hover_start_button_color = (255,255,255)

    # background color
    background_color = (79, 121, 66)
    
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height()

    fonts = pygame.font.get_fonts()
    print(fonts)
    
    # defining a font 
    smallfont = pygame.font.SysFont('impact',35) 
    
    # rendering a text written in 
    # this font 
    text = smallfont.render('quit' , True , font_color) 
    
    while True: 
        
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                    pygame.quit() 
                    
        # fills the screen with a color 
        screen.fill(background_color) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,start_button_color,[width/2,height/2,140,40]) 
            
        else: 
            pygame.draw.rect(screen,hover_start_button_color,[width/2,height/2,140,40]) 
        
        # superimposing the text onto our button 
        screen.blit(text , (width/2+50,height/2)) 
        
        # updates the frames of the game 
        pygame.display.update() 