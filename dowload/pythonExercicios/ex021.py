import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.load('winner.mp3')
pygame.mixer.music.play()

pygame.event.wait()