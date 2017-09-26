import pygame, random, math

class Picture():
    def __init__(self, screen):
        
        self.CIRCLES_LIST = []
        self.CIRCLES_RECT_LIST = []
        self.ANGLES_LIST = [0, 0, 90, 30, 180]
        self.DO_ROTATE_LIST = [0, 0, 0, 0, 0]
        
        self.DO_ROTATE_PLAYER = [False, False, False, False, False]
        self.ROTATE_PLAYER_NUM = [10, 10, 10]
        
        self.count = 0
        circle = pygame.image.load("Circles/Circle_11111.png")
        circle_rect = circle.get_rect()
        circle_rect.center = [600, 400]
        
        self.CIRCLES_LIST.append(circle)
        self.CIRCLES_RECT_LIST.append(circle_rect)
        
        circle = pygame.image.load("Circles/Circle_22222.png")
        self.CIRCLES_LIST.append(circle)
        self.CIRCLES_RECT_LIST.append(circle_rect)
        
        circle = pygame.image.load("Circles/Circle_33333.png")
        self.CIRCLES_LIST.append(circle)
        self.CIRCLES_RECT_LIST.append(circle_rect)
        
        circle = pygame.image.load("Circles/Circle_44444.png")
        self.CIRCLES_LIST.append(circle)
        self.CIRCLES_RECT_LIST.append(circle_rect)
        
        circle = pygame.image.load("Circles/Circle_55555.2.png")
        self.CIRCLES_LIST.append(circle)
        self.CIRCLES_RECT_LIST.append(circle_rect)
                
        
        self.SCREEN = screen
        self.rotate_player = False


    def drawPicture(self):
        
        for list_num in range(0, len(self.CIRCLES_LIST)):
            
            circle = self.CIRCLES_LIST[list_num]
            circle_rect = self.CIRCLES_RECT_LIST[list_num]
            angle = self.ANGLES_LIST[list_num]
            
            circle, circle_rect = self.rot_center(circle, circle_rect, angle)

            self.SCREEN.blit(circle, circle_rect)
            
            
    def newRotatePicture(self, num, newRotate, player):
        
        if newRotate == True:
            self.DO_ROTATE_LIST[num] = True
            
            self.checkIfRotatePlayer(player)
            
    def rotatePicture(self, player):
                
        if self.DO_ROTATE_LIST[2] == True:
            self.ANGLES_LIST[2] -= 1.5
            
            self.isRotatePlayer(2, player, 1.5)
            
            if self.ANGLES_LIST[2] % 45 == 0:
                self.DO_ROTATE_LIST[2] = False
                
        elif self.DO_ROTATE_LIST[3] == True:
            self.ANGLES_LIST[3] += 2
            
            self.isRotatePlayer(3, player, -2)
            
            if self.ANGLES_LIST[3] % 60 == 0:
                self.DO_ROTATE_LIST[3] = False
                
        elif self.DO_ROTATE_LIST[4] == True:
            self.ANGLES_LIST[4] -= 4
            
            self.isRotatePlayer(4, player, 4)
            
            if self.ANGLES_LIST[4] % 120 == 0:
                self.DO_ROTATE_LIST[4] = False

        elif self.DO_ROTATE_LIST[1] == True:
            self.ANGLES_LIST[1] += 1.2
            self.count += 1
            
            self.isRotatePlayer(1, player, -1.2)
            
            if self.count == 30:
                self.count = 0
                self.DO_ROTATE_LIST[1] = False
                
        else:
            self.DO_ROTATE_PLAYER = []
                
            
    def isRotatePlayer(self, num, player, angle):
        
        for list_num in range(0, len(self.DO_ROTATE_PLAYER)):
        
            List = self.DO_ROTATE_PLAYER[list_num]
        
            is_circle = List[0]
            is_player = List[1]
            
            for list_num in range(0, len(player.PLAYER_IMAGE_RECT_LIST)):
                
                if is_circle == num and is_player == list_num:
                    self.movePlayerFromRotate(player, list_num, angle)
            
    def checkIfRotatePlayer(self, player):
        
        center_x = 600
        center_y = 400
                
        for list_num in range(0, len(player.PLAYER_IMAGE_RECT_LIST)):
            player_x, player_y = player.PLAYER_IMAGE_RECT_LIST[list_num].center
            
            distance = math.sqrt(math.pow((center_x - player_x), 2) + math.pow((center_y - player_y), 2));
    
            if distance >= 35 and distance <= 120 and self.DO_ROTATE_LIST[4] == True:
                self.DO_ROTATE_PLAYER.append([4, list_num])
                
            elif distance >= 120 and distance <= 185 and self.DO_ROTATE_LIST[3] == True:
                self.DO_ROTATE_PLAYER.append([3, list_num])
                
            elif distance >= 185 and distance <= 255 and self.DO_ROTATE_LIST[2] == True:
                self.DO_ROTATE_PLAYER.append([2, list_num])
                
            elif distance >= 255 and distance <= 335 and self.DO_ROTATE_LIST[1] == True:
                self.DO_ROTATE_PLAYER.append([1, list_num])
                
    def movePlayerFromRotate(self, player, player_num, angle):
        
        rect_x, rect_y = player.PLAYER_IMAGE_RECT_LIST[player_num].center
        center_x, center_y = self.CIRCLES_RECT_LIST[player_num].center
        angle = math.radians(angle)            
        new_x = math.cos(angle) * (rect_x - center_x) - math.sin(angle) * (rect_y - center_y) + center_x
        new_y = math.sin(angle) * (rect_x - center_x) + math.cos(angle) * (rect_y - center_y) + center_y
       
        player.PLAYER_IMAGE_RECT_LIST[player_num].center = [new_x, new_y]
        
        
    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
        