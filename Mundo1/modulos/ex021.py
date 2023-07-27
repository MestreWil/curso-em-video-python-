import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('lux-aeterna-by-clint-mansell-(mp3convert.org).mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
