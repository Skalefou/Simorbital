import pygame
from celestialBody import CelestialBody
from constante import *

#TODO: Add text to be displayed over the celestials bodys

class Program:
    def __init__(self):
        self.celestialBody = [CelestialBody("Sun", 0, SUN_RADIUS, COLOR_SUN), CelestialBody("Earth", DISTANCE_SUN_EARTH, EARTH_RADIUS, COLOR_EARTH)]
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        pygame.init()
        pygame.display.set_caption("Simorbital")
    
    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            
            i = 0
            for i in range(len(self.celestialBody)):
                self.celestialBody[i].draw(self.screen)
            
            pygame.display.flip()

    def __del__(self):
        pygame.quit()
        

program = Program()
program.run()