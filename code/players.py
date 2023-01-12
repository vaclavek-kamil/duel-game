import pygame
from settings import *

class Player1 (pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.image.load('../art/player/p1-idle.png').get_rect(topleft = pos)
        self.hitbox = pygame.Rect(pos[0], pos[1]+40, 36, 84)
        self.img_idle = pygame.image.load('../art/player/p1-idle.png')
        self.img_move1 = pygame.image.load('../art/player/p1-walk1.png')
        self.img_move2 = pygame.image.load('../art/player/p1-walk2.png')
        self.img_attack1 = pygame.image.load('../art/player/p1-attack1.png')
        self.img_attack2 = pygame.image.load('../art/player/p1-idle.png')

        self.state = 'idle' #idle, walking right, walking left, attacking
        self.idle_facing = 'right'

        #used for the player movement
        self.x_energy = 0
        self.y_energy = 0

        self.SPEED = 5
        self.ACCELERATION = 0.5
        self.GRAVITY = 0.4
        self.JUMP = 10

        self.step = 0
        self.STEP_LENGTH = 15

        #used for the attack and its charging
        self.charge = 0
        self.CHARGE_SPEED = 20
        self.hit = 0
        self.HIT_SPEED = 10


    def update(self, level):
       
        #applying the directional vectors onto the players position and checking for colisions on x and y sepparately

        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.rect.x += self.x_energy
        self.hitbox.x += self.x_energy

        x_collision = 'none'

        for sprite in level.obstacles_sprites:

            if sprite.rect.colliderect(self.hitbox):

                if self.x_energy > 0:
                    x_collision = 'right'
                    self.hitbox.right = sprite.rect.left
                    self.rect.right = sprite.rect.left + 88
                    self.x_energy = 0 

                if self.x_energy < 0:
                    x_collision = 'left'
                    self.hitbox.left = sprite.rect.right
                    self.rect.left = sprite.rect.right
                    self.x_energy = 0

        #yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
        self.rect.y += self.y_energy
        self.hitbox.y += self.y_energy

        y_collision = 'none'

        for sprite in level.obstacles_sprites:

            if sprite.rect.colliderect(self.hitbox):

                if self.y_energy > 0:
                    y_collision = 'bottom'
                    self.hitbox.bottom = sprite.rect.top
                    self.rect.bottom = sprite.rect.top 
                    self.y_energy = 0

                if self.y_energy < 0:
                    y_collision = 'top'
                    self.hitbox.top = sprite.rect.bottom
                    self.rect.top = sprite.rect.bottom - 40
                    self.y_energy = 0

#moving the player right
        if level.pressed_keys[pygame.K_d] and self.x_energy < self.SPEED:
            self.x_energy += self.ACCELERATION
            if self.x_energy > self.SPEED:
                self.x_energy = self.SPEED
        
        #moving the player left
        if level.pressed_keys[pygame.K_a] and self.x_energy > (self.SPEED)*-1:
            self.x_energy -= self.ACCELERATION
            if self.y_energy < (self.SPEED)*-1:
                self.y_energy = (self.SPEED)*-1

        #slowing the player down on no input and laving his direction for later use with idle rendering
        if not level.pressed_keys[pygame.K_a] and not level.pressed_keys[pygame.K_d] and self.x_energy != 0:
            
        

            if self.x_energy > 0:
                self.x_energy -= self.ACCELERATION
                if self.x_energy < 0: self.x_energy = 0
                self.idle_facing = 'right'   
            
            elif self.x_energy < 0:
                self.x_energy += self.ACCELERATION
                if self.x_energy > 0: self.x_energy = 0
                self.idle_facing = 'left'

        


        #Applying gravity
        if y_collision != 'bottom':
            self.y_energy += self.GRAVITY

        #jumping
        if level.pressed_keys[pygame.K_w] and y_collision == 'bottom':
            self.y_energy -= self.JUMP


        

        #deciding the player state (ADD DETECTION OF COLISION TO WALKING LEFT AND RIGHT)
        if level.pressed_keys[pygame.K_d]:
            self.state = 'walking right'

        elif level.pressed_keys[pygame.K_a]:
            self.state = 'walking left'

        else:
            self.state = 'idle'
       
    def custom_draw(self, level):
        #WALKING
        if self.state == 'walking right' or self.state == 'walking left':
            self.step += 1
            if self.step > self.STEP_LENGTH:
                self.step = 0
        
        #changing feet for walking right
        if self.state == 'walking right' and self.step < self.STEP_LENGTH/2:
            level.display_surface.blit(self.img_move1, self.rect)
        elif self.state == 'walking right':
            level.display_surface.blit(self.img_move2, self.rect)

        #changing feet for waling left
        offset_rect = self.img_move1.get_rect(topleft = self.rect.topleft)
        offset_rect.x -= 88

        if self.state == 'walking left' and self.step < self.STEP_LENGTH/2:
            level.display_surface.blit(pygame.transform.flip(self.img_move1, True, False), offset_rect)
            
        elif self.state == 'walking left':
            level.display_surface.blit(pygame.transform.flip(self.img_move2, True, False), offset_rect)
            
        #IDLING
        elif self.state == 'idle':
            if self.idle_facing == 'right':
                level.display_surface.blit(self.img_idle, self.rect)

            else:
                level.display_surface.blit(pygame.transform.flip(self.img_idle, True, False), offset_rect)

        #Debug outline for the player hitbox
        #
        #
        #
        pygame.draw.rect(level.display_surface, (255,255,0), self.hitbox, 3)


######################################################################################
######################################################################################
######################################################################################

class Player2 (pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.image.load('../art/player/p1-idle.png').get_rect(topleft = pos)
        self.hitbox = pygame.Rect(pos[0], pos[1]+40, 36, 84)
        self.img_idle = pygame.image.load('../art/player/p2-idle.png')
        self.img_move1 = pygame.image.load('../art/player/p2-walk1.png')
        self.img_move2 = pygame.image.load('../art/player/p2-walk2.png')
        self.img_attack1 = pygame.image.load('../art/player/p2-attack1.png')
        self.img_attack2 = pygame.image.load('../art/player/p2-idle.png')

        self.state = 'idle' #idle, walking right, walking left, attacking
        self.idle_facing = 'right'

        #used for the player movement
        self.x_energy = 0
        self.y_energy = 0

        self.SPEED = 5
        self.ACCELERATION = 0.5
        self.GRAVITY = 0.4
        self.JUMP = 10

        self.step = 0
        self.STEP_LENGTH = 15

        #used for the attack and its charging
        self.charge = 0
        self.CHARGE_SPEED = 20
        self.hit = 0
        self.HIT_SPEED = 10


    def update(self, level):
       
        #applying the directional vectors onto the players position and checking for colisions on x and y sepparately

        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.rect.x += self.x_energy
        self.hitbox.x += self.x_energy

        x_collision = 'none'

        for sprite in level.obstacles_sprites:

            if sprite.rect.colliderect(self.hitbox):

                if self.x_energy > 0:
                    x_collision = 'right'
                    self.hitbox.right = sprite.rect.left
                    self.rect.right = sprite.rect.left + 88
                    self.x_energy = 0 

                if self.x_energy < 0:
                    x_collision = 'left'
                    self.hitbox.left = sprite.rect.right
                    self.rect.left = sprite.rect.right
                    self.x_energy = 0

        #yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
        self.rect.y += self.y_energy
        self.hitbox.y += self.y_energy

        y_collision = 'none'

        for sprite in level.obstacles_sprites:

            if sprite.rect.colliderect(self.hitbox):

                if self.y_energy > 0:
                    y_collision = 'bottom'
                    self.hitbox.bottom = sprite.rect.top
                    self.rect.bottom = sprite.rect.top 
                    self.y_energy = 0

                if self.y_energy < 0:
                    y_collision = 'top'
                    self.hitbox.top = sprite.rect.bottom
                    self.rect.top = sprite.rect.bottom - 40
                    self.y_energy = 0

#moving the player right
        if level.pressed_keys[pygame.K_RIGHT] and self.x_energy < self.SPEED:
            self.x_energy += self.ACCELERATION
            if self.x_energy > self.SPEED:
                self.x_energy = self.SPEED
        
        #moving the player left
        if level.pressed_keys[pygame.K_LEFT] and self.x_energy > (self.SPEED)*-1:
            self.x_energy -= self.ACCELERATION
            if self.y_energy < (self.SPEED)*-1:
                self.y_energy = (self.SPEED)*-1

        #slowing the player down on no input and laving his direction for later use with idle rendering
        if not level.pressed_keys[pygame.K_LEFT] and not level.pressed_keys[pygame.K_RIGHT] and self.x_energy != 0:
            
        

            if self.x_energy > 0:
                self.x_energy -= self.ACCELERATION
                if self.x_energy < 0: self.x_energy = 0
                self.idle_facing = 'right'   
            
            elif self.x_energy < 0:
                self.x_energy += self.ACCELERATION
                if self.x_energy > 0: self.x_energy = 0
                self.idle_facing = 'left'

        


        #Applying gravity
        if y_collision != 'bottom':
            self.y_energy += self.GRAVITY

        #jumping
        if level.pressed_keys[pygame.K_UP] and y_collision == 'bottom':
            self.y_energy -= self.JUMP


        

        #deciding the player state (ADD DETECTION OF COLISION TO WALKING LEFT AND RIGHT)
        if level.pressed_keys[pygame.K_RIGHT]:
            self.state = 'walking right'

        elif level.pressed_keys[pygame.K_LEFT]:
            self.state = 'walking left'

        else:
            self.state = 'idle'
       
    def custom_draw(self, level):
        #WALKING
        if self.state == 'walking right' or self.state == 'walking left':
            self.step += 1
            if self.step > self.STEP_LENGTH:
                self.step = 0
        
        #changing feet for walking right
        if self.state == 'walking right' and self.step < self.STEP_LENGTH/2:
            level.display_surface.blit(self.img_move1, self.rect)
        elif self.state == 'walking right':
            level.display_surface.blit(self.img_move2, self.rect)

        #changing feet for waling left
        offset_rect = self.img_move1.get_rect(topleft = self.rect.topleft)
        offset_rect.x -= 88

        if self.state == 'walking left' and self.step < self.STEP_LENGTH/2:
            level.display_surface.blit(pygame.transform.flip(self.img_move1, True, False), offset_rect)
            
        elif self.state == 'walking left':
            level.display_surface.blit(pygame.transform.flip(self.img_move2, True, False), offset_rect)
            
        #IDLING
        elif self.state == 'idle':
            if self.idle_facing == 'right':
                level.display_surface.blit(self.img_idle, self.rect)

            else:
                level.display_surface.blit(pygame.transform.flip(self.img_idle, True, False), offset_rect)

        #Debug outline for the player hitbox
        #
        #
        #
        pygame.draw.rect(level.display_surface, (255,255,0), self.hitbox, 3)


######################################################################################
######################################################################################
######################################################################################