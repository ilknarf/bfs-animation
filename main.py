import sys
import pygame
from collections import deque, defaultdict

pygame.init()
clock = pygame.time.Clock()

size = width, height, = 800, 400

screen = pygame.display.set_mode(size)

black = 0, 0, 0
white = (255, 255, 255)
gray = (200, 200, 200)
green = (141,182,0)
goal = (3,5)
start = (15, 9)

class Grid:
    def __init__(self, goal):
        self.colors = (black, white, green)

    def draw(self, coord):
        for x,y in coord:
            pygame.draw.rect(screen, white, 
                pygame.Rect(x*40, y*40, 40, 40), 0)

        pygame.draw.rect(screen, green, 
                pygame.Rect(goal[0]*40, goal[1]*40, 40, 40), 0)
g = Grid(goal)
back = {}
stack = deque()
stack.append(start)

found = False
c = goal

def add_next(stack, coord):
    x, y = coord
    if x < 20:
        c = (x+1, y)
        if not back.get(c):
            back[c] = coord
            stack.append(c)
    if y < 10:
        c = (x, y+1)
        if not back.get(c):
            back[c] = coord
            stack.append(c)
    if x > 0:
        c = (x-1, y)
        if not back.get(c):
            back[c] = coord
            stack.append(c)
    if y > 0:
        c = (x, y-1)
        if not back.get(c):
            back[c] = coord
            stack.append(c)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if not found:
        c = stack.popleft()
        if c == goal:
            found = True
        else: 
            add_next(stack, c)

        g.draw(back.keys())
    else:

        pygame.draw.rect(screen, green, 
                pygame.Rect(c[0]*40, c[1]*40, 40, 40), 0)
        if c != start:
            c = back[c]

    pygame.display.flip()
    clock.tick(60)