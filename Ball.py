import pygame
import random

ballSprite = "ball.gif"

class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self) # Sprite init
        self.image = pygame.image.load(ballSprite).convert()
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, self.game.screen.get_size()[0] - self.rect.width)
        self.rect.y = random.randrange(0, self.game.screen.get_size()[1] - self.rect.height)

        
        
