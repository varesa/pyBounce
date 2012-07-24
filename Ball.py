import pygame

ballSprite = "ball.gif"

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Sprite init
        self.image = pygame.image.load(ballSprite).convert()
        self.rect = self.image.get_rect()
