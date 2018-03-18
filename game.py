import pygame,random,math,PygButton
from Spinner import Spinner
from Dice import Dice
from Label import Label
from Picture import Picture
from Photo import Photo
from Player import Player

pygame.init()

class Game():

    def game(self, screen, background):
        music = pygame.mixer.music
        music.load("files/music.ogg")
        music.play(-1)


        RULES_rect = pygame.Rect(80, 740, 100, 50)
        NEXT_TURN_rect = pygame.Rect(220, 740, 100, 50)
        self.NEXT_TURN = PygButton.PygButton(NEXT_TURN_rect, 'Next Turn', (0,0,0), (255,0,0), pygame.font.SysFont("Verdana", 18))
        self.RULES = PygButton.PygButton(RULES_rect, 'Rules', (0,0,0), (255,0,0), pygame.font.SysFont("Verdana", 20))


        self.spinner = Spinner(screen)
        self.dice = Dice(screen, 140, 225)
        self.dice2 = Dice(screen, 140, 285)

        self.ANGLE = 0
        self.SPINS_TILL_DONE = 0
        self.DICE_TILL_DONE = 0
        self.showDiceNum = 0
        self.showDiceNum2 = 1
        self.switchDie = 0
    
        self.player = Player(screen)
        self.PLAYER_TURN = 0
        self.MOVE_SPEED = 20
        self.movePlayer = False
        self.PLAYER_MOVE_X = 0
        self.PLAYER_MOVE_Y = 0
        
        picture = Picture(screen)
    
        n = True
        
        keep_going = True
        clock = pygame.time.Clock()
        hideRules = True
        muteState = False
    
        while keep_going:
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        hideRules = True
                    elif event.key == pygame.K_ESCAPE:
                        keep_going = False
                    elif event.key == pygame.K_q:
                        keep_going = False
                    elif event.key == pygame.K_p:
                        if muteState==False:
                            music.pause()
                            muteState = True
                        else:
                            music.unpause()
                            muteState = False
                                                
                if event.type == pygame.MOUSEBUTTONUP:     
                                       
                    x, y = pygame.mouse.get_pos()
            #        print (x)
            #        print (y)
                                       
                    spin = self.checkDoSpinner()
                    
                    if spin == False:
                        dice = self.checkDoDice()
                        
                        if dice == False:
                            self.movePlayer = True
                                    
                            x, y = pygame.mouse.get_pos()
                            self.PLAYER_MOVE_X = x
                            self.PLAYER_MOVE_Y = y
                            
                            
                    self.distance()
                    
                if 'click' in self.NEXT_TURN.handleEvent(event):
                    
                    self.movePlayer = False
                    
                    if self.PLAYER_TURN == 2:
                        self.PLAYER_TURN = 0
                    else:
                        self.PLAYER_TURN += 1
                #    print ("CLICKED")
                  #  if random.randint(0, 1) == 0:
                    
                    picture.newRotatePicture(random.randint(1, 4), True, self.player)


                if 'click' in self.RULES.handleEvent(event):
                    hideRules = False
                    self.movePlayer = False
                    
            screen.blit(background, (0, 0)) 

            circus = ("C","","R","C","U","S")
            circles= ("C","","R","C","L","E","S")

            if hideRules:
                picture.drawPicture()
                picture.rotatePicture(self.player)
                self.NEXT_TURN.draw(screen)
                self.RULES.draw(screen)
                for i in range(0,6):
                    Label(screen,circus[i],80,50,230 + i*80)
                for i in range(0,7):
                    Label(screen,circles[i],80,1100,200 + i*80)
                Label(screen,"I",80,60,310)
                Label(screen,"I",80,1110,280)
                Label(screen,"Player 1",25,150,700)
                Label(screen,"Player 2",25,950,70)
                Label(screen,"Player 3",25,910,750)
                self.spinnerAnimation()
                self.diceAnimation()
                self.playerAnimation()


            else:
                Photo(screen,"files/rules.png",0,0)
    
            pygame.display.flip()
        #music.stop()
    
    
    def checkDoSpinner(self):
        
        x, y = pygame.mouse.get_pos()
                    
        x1 = self.spinner.SPINNER_CIRCLE_RECT.x + (self.spinner.SPINNER_CIRCLE_WIDTH / 2)
        y1 = self.spinner.SPINNER_CIRCLE_RECT.y + (self.spinner.SPINNER_CIRCLE_HEIGHT / 2)

        distance = math.sqrt(math.pow((x - x1), 2) + math.pow((y - y1), 2));
     #   print "SPinner   ",(distance)
        if distance <= 100:
            self.SPINS_TILL_DONE = random.randint(18, 26)
            return True
        else:
            return False
            
    def checkDoDice(self):
        
        x, y = pygame.mouse.get_pos()
                    
        x1 = self.dice.DICE_RECT.x + (self.dice.DICE_WIDTH / 2)
        y1 = self.dice.DICE_RECT.y + (self.dice.DICE_HEIGHT / 2)

        distance = math.sqrt(math.pow((x - x1), 2) + math.pow((y - y1), 2));
        
        x2 = self.dice2.DICE_RECT.x + (self.dice2.DICE_WIDTH / 2)
        y2 = self.dice2.DICE_RECT.y + (self.dice2.DICE_HEIGHT / 2)

        distance2 = math.sqrt(math.pow((x - x2), 2) + math.pow((y - y2), 2));
        
    #    print "dice    ",(distance)
        if distance <= 35 or distance2 <= 35:
            self.switchDie = 0
            self.DICE_TILL_DONE = 12
            return True
        else:
            return False

    def spinnerAnimation(self):
        
        self.spinner.drawCircle()
        self.spinner.drawSpinner(self.ANGLE)
        
        if self.SPINS_TILL_DONE >= 2:

            num = random.randint(0, 10)
            
            if num == 0:
                self.SPINS_TILL_DONE -= 2
            
            self.ANGLE += self.SPINS_TILL_DONE
            
    def diceAnimation(self):
        
        self.dice.drawDice(self.showDiceNum)
        self.dice2.drawDice(self.showDiceNum2)
        
        if self.DICE_TILL_DONE >= 6:
            
            self.switchDie += 20
            
            if 60 - self.switchDie <= 0:
                self.switchDie = 0
                self.DICE_TILL_DONE -= 1
                self.showDiceNum = random.randint(0, 5)
                self.showDiceNum2 = random.randint(1, 4)
                
    def playerAnimation(self):
        
        self.player.drawPlayers()
        
        x = self.PLAYER_MOVE_X
        y = self.PLAYER_MOVE_Y
                                        
        player_x, player_y = self.player.PLAYER_IMAGE_RECT_LIST[self.PLAYER_TURN].center
            
        distance = math.sqrt(math.pow((x - player_x), 2) + math.pow((y - player_y), 2));

        if distance >= 10 and self.movePlayer == True:
            
            angle = math.atan2(y - player_y, x - player_x)
            
            new_x = math.cos(angle) * self.MOVE_SPEED     
            new_y = math.sin(angle) * self.MOVE_SPEED    
            
            self.player.movePlayer(self.PLAYER_TURN, new_x, new_y) 
            
        else:
            self.movePlayer = False
            
            
    def distance(self):
        x, y = pygame.mouse.get_pos()
        distance = math.sqrt(math.pow((600 - x), 2) + math.pow((400 - y), 2))
    #    print ("distance   ",distance)
        
        new_x = (math.cos(45) * (x - 600)) - (math.sin(45) * (y - 400)) + 600
        
        new_y = (math.sin(45) * (x - 600)) + (math.cos(45) * (y - 400)) + 400

    #    print ("new x   :", new_x)
    #    print ("new y   :", new_y)
        
        
def main():
    screen = pygame.display.set_mode((1200, 800),pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Game!')
    background = pygame.Surface(screen.get_size()) 
    background.fill((255 , 255, 255)) 

    
    g = Game()
    g.game(screen, background)

main()