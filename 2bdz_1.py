import pygame
from math import sin, cos
from math import pi


class Canvas:
    def __init__(self, scene, size):
        self.width = width
        self.height = height
        # self.render(scene)

    def render(self, scene, coords):
        pygame.draw.rect(scene, 'black', (0, 0, self.width, self.height), width=300)
        # pygame.draw.rect(scene, 'white', (0, 0, self.width, self.height), width=5)

    def change(self, scene, coords, center_coords):
        pygame.draw.rect(scene, 'black', (0, 0, self.width, self.height), width=300)
        pygame.draw.circle(scene, 'red', center_coords, 2 * radius)
        pygame.draw.line(scene, 'white', center_coords, coords)
        pygame.draw.circle(scene, 'white', (coords[0], coords[1]), 2 * radius)


width = 600
height = 600
radius = 2
size = 200

g = 9.81 * size
l = 1 * size
phi0 = pi / 6
w = (g / l) ** 0.5 * size
dt = 1 / 10000
t = 0

screen = pygame.display.set_mode((width, height))
canvas = Canvas(screen, width)
running = True
clock = pygame.time.Clock()
fps = 60
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += dt

    phi = phi0 * cos(w * t)
    x = -l * sin(phi) + 300
    y = l * cos(phi) + 300

    canvas.change(screen, (x, y), (300, 300))
    pygame.display.flip()
