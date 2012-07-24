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

        self.xvel = random.randrange(-10, 10)
        self.yvel = random.randrange(-10, 10)

    def update(self):
        self.detectCollisions()
        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def detectCollisions(self):
        if self.rect.x <= 0 or self.rect.x >= self.game.screen.get_size()[0] - self.rect.width:
            self.xvel *= -1
        if self.rect.y <= 0 or self.rect.y >= self.game.screen.get_size()[1] - self.rect.height:
            self.yvel *= -1
        
