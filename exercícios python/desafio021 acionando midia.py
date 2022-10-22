import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('wire.mpeg')
pygame.mixer.music.play()
pygame.event.wait()