import pygame , sys
import numpy as np
ROWS = 40
COLS = 8
def hex_screen(screen):
    for i in range(ROWS-1,-1,-1):
        value = ""
        for row in screen:
            value+=str(row[i])
        hex_value = str(hex(eval("0b"+value)))[2:]
        print(hex_value, end = " ")
    print()



scale = 50
WIDTH = ROWS * scale
HEIGHT = COLS *scale
pygame.init()
clock = pygame.time.Clock()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
OFF_COLOR = (64,64,64)
ON_COLOR = (0,255,0)
SCREEN = [[0 for i in range(ROWS)] for i in range(COLS)]
run = True
p_clicked = False
while run:
    clock.tick(120)
    pygame.display.update()
    SURFACE.fill(OFF_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
            
    # Logic is Here
    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        SCREEN[y//scale][x//scale] = 1
    
    if pygame.mouse.get_pressed()[2]:
        SCREEN[y//scale][x//scale] = 0
    
    if pygame.key.get_pressed()[pygame.K_p] and not p_clicked:
        p_clicked = True
        hex_screen(SCREEN)
    if not pygame.key.get_pressed()[pygame.K_p]:
        p_clicked = False
    
    for col in range(0,ROWS):
        for row in range(0,COLS):
            # col = 31-col
            if SCREEN[row][col] == 1:
                pygame.draw.rect(SURFACE, ON_COLOR, (col*scale, row*scale, scale, scale))
            pygame.draw.line(SURFACE, (0,0,0), (col*scale, 0), (col*scale, HEIGHT))
            pygame.draw.line(SURFACE, (0,0,0), (0, row*scale), (WIDTH, row*scale))


hex_screen(SCREEN)

sys.exit()