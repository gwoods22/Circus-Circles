'''
Created on Apr 5, 2016

@author: ryan3971
'''

import pygame

class Spinner():
    
    def __init__(self, screen):
        
        self.SCREEN = screen
        
        self.SPINNER_CIRCLE = pygame.image.load("files/spinner_complete.png")
        self.SPINNER_CIRCLE_RECT = self.SPINNER_CIRCLE.get_rect()
        self.SPINNER_CIRCLE_RECT.y = 0
        self.SPINNER_CIRCLE_RECT.x = 0
        
        self.SPINNER = pygame.image.load("files/ar.png")
        self.SPINNER_RECT = self.SPINNER.get_rect()
        self.SPINNER_RECT.y = 40
        self.SPINNER_RECT.x = 102

        self.SPINNER_CIRCLE_WIDTH = self.SPINNER_CIRCLE.get_width()
        self.SPINNER_CIRCLE_HEIGHT = self.SPINNER_CIRCLE.get_height()

    
    def drawCircle(self):
        self.SCREEN.blit(self.SPINNER_CIRCLE, self.SPINNER_CIRCLE_RECT)
            
    def drawSpinner(self, angle):
        spinner, rect = self.rot_center(self.SPINNER, self.SPINNER_RECT, angle)
        self.SCREEN.blit(spinner, rect)
        
    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

