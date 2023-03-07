import pygame
from math import sin, cos
from math import pi, e


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def change(self, scene, coords, center_coords):
        pygame.draw.rect(scene, 'black', (0, 0, self.width, self.height), width=300)
        pygame.draw.circle(scene, 'red', center_coords, 2 * radius)
        pygame.draw.line(scene, 'white', center_coords, coords)
        pygame.draw.circle(scene, 'white', (coords[0], coords[1]), 2 * radius)


# 200 пикселей = 1 м
width = 600
height = 600
radius = 2
size = 200

g = 9.81 * size  # м / с ^ 2
l = 1 * size  # м
phi = pi - 0.1  # radians
beta = 0.1  # 1 / c
q = 0

w = ((g / l) - beta ** 2) ** 0.5  # 1 / c
wcenter = 5
acenter = 50
dt = 1 / 500  # c
t = 0

screen = pygame.display.set_mode((width, height))
pygame.init()
font = pygame.font.SysFont('latex', 30)
text = font.render('t = 0 c', True, 'white', 'black')
textRect = text.get_rect()
textRect.center = (500, 50)

canvas = Canvas(width, height)
running = True
flag = True
clock = pygame.time.Clock()
while running:
    clock.tick(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flag = False if flag else True

    if flag:
        q -= dt * (g / l * sin(phi) + 2 * beta * q)

        phi += dt * q

        x = l * sin(phi) + width / 2
        y = l * cos(phi) + height / 2

        t += dt

        canvas.change(screen, (x, y), (300, 300))
        text = font.render(f't = {round(t, 3)} c', True, 'white', 'black')
        screen.blit(text, textRect)
        pygame.display.flip()
