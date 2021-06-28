# Name: Charmi Kadi
# Date: June. 24, 2021
# Course Code: ICS3U1-01
# Description: Graphics exercises

import pygame 

BLUE = (17, 172, 250)
PINK = (255, 117, 234)

pygame.init()
SIZE = (500, 500)
screen = pygame.display.set_mode(SIZE)

while True:
    screen.fill(BLUE)
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, PINK, pygame.Rect(200, 200, 100, 100))
    

    pygame.display.flip()
    pygame.time.wait(500)

pygame.quit()