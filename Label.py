import pygame

class Label():
    def __init__(self,screen,text,fontSize,x,y):
        self.screen = screen
        self.text = text
        self.font = pygame.font.SysFont("Verdana", fontSize)
        self.image = self.font.render(self.text, 1, (255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image,self.rect)
