import pygame, sys
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
size = (300, 300)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('teclado')
running = True

def play(note):
    from time import sleep
    from os import path
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, size[0], size[1]], 0)

    font = pygame.font.SysFont('Comic Sans MS', 60)
    textSurface = font.render(note, False, (255, 255, 255))
    screen.blit(textSurface, (size[0] / 2, size[1] / 2))

    file = path.join('assets', f'{note}.wav')
    soundObj = pygame.mixer.Sound(file)
    soundObj.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            triggers = {
                'a': lambda: play('do'), 
                'd': lambda: play('mi'),
                'f': lambda: play('fa'),
                's': lambda: play('re'),
                'g': lambda: play('sol'),
                'h': lambda: play('la'),
                'j': lambda: play('si'),
                'k': lambda: play('do')
            }
            keyPressed = pygame.key.name(event.key)
            if keyPressed in triggers.keys():
                triggers[keyPressed]()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
