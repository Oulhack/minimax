import sys
import pygame
import numpy as np

pygame.init()

#colors
WHITE=(255,255,255)
GRAY=(180,180,180)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)

#PROPERTIES AND SIZES
WIDTH=300
HEIGHT=300
LINE_WIDTH=5
BRAOD_ROWS=3
BAORD_COLS=3
SQUARE_SIZE =WIDTH // BAORD_COLS
CIRCLE_RADIUS = SQUARE_SIZE //3
CIRCLE_WIDTH=15
CROSS_WIDTH=25

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")
screen.fill(BLACK)



