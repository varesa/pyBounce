import pygame
import sys
import time

from Ball import Ball

numberOfBalls = 1

class Main:
        def init(self):
                pygame.init()
                self.screen = pygame.display.set_mode([800, 600])
                self.clock = pygame.time.Clock()

                balls = []
                for x in range(numberOfBalls):
                        balls.append(Ball(self.screen.get_size()))

                self.objects = []
                self.objects.extend(balls)
                
                self.allsprites = pygame.sprite.RenderPlain(self.objects)

                self.background = pygame.Surface(self.screen.get_size()).convert()
                self.background.fill((250, 250, 250))

        def run(self):
                running = True

                while running:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT: 
                                        running = False
                        self.allsprites.update()
                        self.screen.blit(self.background, (0, 0))
                        self.allsprites.draw(self.screen)
                        pygame.display.flip()
                        self.clock.tick(60)

game = Main()
game.init()
game.run()

