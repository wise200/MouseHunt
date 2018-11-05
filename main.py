from mouse import mouse
import pygame

screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)

flag = True
clock = pygame.time.clock()
framerate = 30

while flag:
	clock.tick(framerate)
	