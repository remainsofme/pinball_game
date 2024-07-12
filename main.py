import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((500,500))
        self.running=True
        self.bouncing=False
        self.ch_direction=False
        self.move_to_left=False
        self.move_to_right=False
        self.game_over=False
        self.mouse_click=False
        self.gravity=(0,2)
        self.speed=(3,5)
        self.board_speed=(0,0)
        self.hit_counter=0
        self.font1=pygame.font.SysFont(None,20)
        self.font2=pygame.font.SysFont(None,50)
        self.hit_counter_text=self.font1.render(str(self.hit_counter),True,(0,0,0))
        self.game_over_text=self.font2.render('Game Over',True,(0,0,0))
        self.restart_text=self.font2.render('Restart',True,(0,0,0))
        self.restart_text_rect=self.restart_text.get_rect(topleft=(5000,5000))
        self.ball=pygame.image.load('pics/ball.jpg').convert_alpha()
        self.ball_rect=self.ball.get_rect(center=(20,20))
        self.board=pygame.image.load('pics/board.png').convert_alpha()
        self.board_rect=self.board.get_rect(center=(250,490))
            
    def calculation(self):
        def change_direction(speed):
            items=[]
            for item in speed:
                items.append(-item)
            print(items)
            return tuple(items)
        def add_speed(speed1,speed2):
            return (speed1[0]+speed2[0],speed1[1]+speed2[1])
        
 
        print(self.speed)
        if self.bouncing==True:
            self.ball_rect.move_ip(self.speed)
        ## make sure ball do not escape field
        if self.ball_rect.x+self.ball_rect.width>=500: 
            self.speed=(-self.speed[0],self.speed[1])
        if self.ball_rect.x<=0:
             self.speed=(-self.speed[0],self.speed[1])
        if self.ball_rect.y+self.ball_rect.height>=500:
             self.game_over=True
        if self.ball_rect.y<=0:
             self.speed=(self.speed[0],-self.speed[1])
             
        ## move board
        if self.move_to_left:
            self.board_rect.move_ip((-7,0))
        if self.move_to_right:
            self.board_rect.move_ip((7,0))
        
        ## make sure board not escaping field
        if self.board_rect.x<=0 or self.board_rect.x+self.board_rect.width>=500:
            self.move_to_left=False
            self.move_to_right=False
        
        ## colide
        if self.ball_rect.colliderect(self.board_rect):
            self.speed=(self.speed[0],-self.speed[1])
            self.hit_counter=self.hit_counter+1
            self.hit_counter_text=self.font1.render(str(self.hit_counter),True,(0,0,0))
            self.speed=(self.speed[0],self.speed[1])
            print(self.hit_counter)
            
        ## restart_button_colide
        if self.game_over:
            self.restart_text_rect=self.restart_text.get_rect(topleft=(150,150))
            mouse_pos=pygame.mouse.get_pos()
            if self.restart_text_rect.collidepoint(mouse_pos) and self.mouse_click:
                self.hit_counter=0
                self.hit_counter_text=self.font1.render(str(self.hit_counter),True,(0,0,0))
                self.game_over=False
                self.board_rect.center=(250,490)
                self.ball_rect.center=(20,20)
                self.restart_text_rect.topleft=(5000,5000)
                self.speed=(4,2)
                print(self.hit_counter)
                
     
    
    def graphic(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.ball,self.ball_rect)
        self.screen.blit(self.board,self.board_rect)
        self.screen.blit(self.hit_counter_text,(10,10))
        if self.game_over:
            self.screen.blit(self.game_over_text,(150,100))
            self.screen.blit(self.restart_text,self.restart_text_rect)
        pygame.display.flip()
        
        
    def trigger(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_k:
                    self.bouncing=not self.bouncing
                if event.key==pygame.K_d:
                    self.move_to_right=True
                if event.key==pygame.K_a:
                    self.move_to_left=True                
                    
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_k:
                    #self.bouncing=False
                    pass    
                if event.key==pygame.K_d:
                    self.move_to_right=False
                if event.key==pygame.K_a:
                    self.move_to_left=False     
            if event.type==pygame.MOUSEBUTTONDOWN:
                self.mouse_click=True
            if event.type==pygame.MOUSEBUTTONUP:
                self.mouse_click=False
                    
             
    
    
    def main(self):
         self.calculation()
         self.trigger()
         self.graphic()
         self.clock.tick(60)
        
        
if __name__== '__main__':
    game=Game()
    while game.running:
        game.main()
        
    
        
    