import string
from tracemalloc import start
import pygame as pg, sys

class Button:
    background_color = (0, 0, 0)
    font:string
    font_color = (0, 0, 0)
    font_size:int
    width:int
    height:int
    position_x:int
    position_y:int
    text:string

    def __init__(self, some_background_color, some_font:string, some_font_color, some_font_size:int, some_width:int, some_height:int, some_position_x:int, some_position_y:int, some_text:string):
        """
        Adds values to the parameters when a new Button is created.

        Parameters
        ----------
        some_background_color, some_font, some_font_color, font_size, some_width, some_height, some_position_x, some_position_y, some_text
        """
        self.background_color = some_background_color
        self.font = some_font
        self.font_color = some_font_color
        self.font_size = some_font_size
        self.width = some_width
        self.height = some_height
        self.position_x = some_position_x
        self.position_y = some_position_y
        self.text = some_text

    def createButton(self, screen) -> None:
        """Creates the button on the screen.

        Parameters
        ----------
        width - width of the button

        height - height of the button

        background_color - color of the button

        x - x position of the button on the screen

        y - y position of the button on the screen

        screen - needed for .rect(...), describes the size of the screen
        """
        pg.draw.rect(screen, self.background_color, pg.Rect(self.height, self.width, self.position_x, self.position_y))


pg.init()
screen_resolution = (800, 600) 
screen_window = pg.display.set_mode((screen_resolution))
font_color = (0, 0, 0)
start_button_color = (192, 192, 192) 
hover_start_button_color = (255,255,255)
background_color = (79, 121, 66)
screen_width = screen_window.get_width()
screen_height = screen_window.get_height()
fonts = pg.font.get_fonts()

start_button_font = pg.font.SysFont('impact',30)

start_button = Button((250, 250, 250), 'impact', (0, 0, 0), 30, 30, 60, 300, 300, "Button")
start_button.createButton(screen_window)

# creating text for the quit button
text = start_button_font.render('Quit' , True , font_color) 

while True: 
        
        for ev in pg.event.get(): 
            
            if ev.type == pg.QUIT: 
                pg.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pg.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if screen_width/2 <= mouse[0] <= screen_width/2+140 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
                    pg.quit() 
                    
        # fills the screen with a color 
        screen_window.fill(background_color) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pg.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if screen_width/2 <= mouse[0] <= screen_width/2+140 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
            pg.draw.rect(screen_window,start_button_color,[screen_width/2,screen_height/2,140,40]) 
            
        else: 
            pg.draw.rect(screen_window,hover_start_button_color,[screen_width/2,screen_height/2,140,40]) 
        
        # superimposing the text onto our button 
        screen_window.blit(text , (screen_width/2+50,screen_height/2)) 
        
        # updates the frames of the game 
        pg.display.update() 