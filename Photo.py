import pygame

class Photo():
    def __init__(self,screen,photo,x,y):
        self.screen = screen
        self.image = pygame.image.load(photo)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image,self.rect)
