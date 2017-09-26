'''
Created on Apr 6, 2016

@author: ryan3971
'''


import pygame

class Dice():
    
    def __init__(self, screen, x, y):
        
        self.SCREEN = screen
        
        self.DICE_LIST = []
        
        
        self.DICE = pygame.image.load("dice/dice1.png")
        self.DICE_RECT = self.DICE.get_rect()
        self.DICE_RECT.y = y
        self.DICE_RECT.x = x
        
        self.DICE_WIDTH = self.DICE.get_width()
        self.DICE_HEIGHT = self.DICE.get_height()

        self.DICE_LIST.append(self.DICE)
        self.DICE = pygame.image.load("dice/dice2.png")
        self.DICE_LIST.append(self.DICE)
        self.DICE = pygame.image.load("dice/dice3.png")
        self.DICE_LIST.append(self.DICE)
        self.DICE = pygame.image.load("dice/dice4.png")
        self.DICE_LIST.append(self.DICE)
        self.DICE = pygame.image.load("dice/dice5.png")
        self.DICE_LIST.append(self.DICE)
        self.DICE = pygame.image.load("dice/dice6.png")
        self.DICE_LIST.append(self.DICE)
    
    def drawDice(self, list_num):
        
        dice = self.DICE_LIST[list_num]
        self.SCREEN.blit(dice, self.DICE_RECT)
          

