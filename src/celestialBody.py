import pygame
from math import ceil
from constante import *

class CelestialBody:
    def __init__(self, name, distance, radius, color):
        self.name = name
        self.distance = distance
        self.radius = radius
        self.color = color
        
        if self.radius >= 100000:
            self.radiusAbs = ceil((self.radius/8)/800)
        elif self.radius >= 1000:
            self.radiusAbs = ceil(self.radius/500)
        if self.distance != 0:
            self.position = [SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT/2]
        else:
            self.position = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radiusAbs)