'''
Created on Apr 6, 2016

@author: ryan3971
'''

import pygame

class Player():
    
    def __init__(self, screen):
        
        self.SCREEN = screen
        
        self.PLAYER_IMAGE_LIST = []
        self.PLAYER_IMAGE_RECT_LIST = []

        player = pygame.image.load("files/player_1.png")
        player_rect = player.get_rect()
        player_rect.y = 600
        player_rect.x = 145
        self.PLAYER_IMAGE_LIST.append(player)
        self.PLAYER_IMAGE_RECT_LIST.append(player_rect)
        
        player = pygame.image.load("files/player_2.png")
        player_rect = player.get_rect()
        player_rect.y = 120
        player_rect.x = 965
        self.PLAYER_IMAGE_LIST.append(player)
        self.PLAYER_IMAGE_RECT_LIST.append(player_rect)
        
        player = pygame.image.load("files/player_3.png")
        player_rect = player.get_rect()
        player_rect.y = 655
        player_rect.x = 915
        self.PLAYER_IMAGE_LIST.append(player)
        self.PLAYER_IMAGE_RECT_LIST.append(player_rect)
        
        
    def drawPlayers(self):
        for list_num in range(0, len(self.PLAYER_IMAGE_LIST)):
            
            player = self.PLAYER_IMAGE_LIST[list_num]
            player_rect = self.PLAYER_IMAGE_RECT_LIST[list_num]

            self.SCREEN.blit(player, player_rect)
            
    def movePlayer(self, player_num, newX, newY):
        
        player_rect = self.PLAYER_IMAGE_RECT_LIST[player_num]
        
        player_rect.x += newX
        player_rect.y += newY
        
        self.PLAYER_IMAGE_RECT_LIST[player_num] = player_rect
            