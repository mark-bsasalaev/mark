import pygame
import random
 
class Rect:
    def __init__(self, x, y, dx, width, height, s):
      self.x = x 
      self.y = y
      self.dx = dx
      self.width = width
      self.height = height
      self.s = s
    
    def die(self):
      self.x = -100
      self.y = -100
      self.s = False
      
def kill_roket():
    global rx, rs, rs
    rx = -100
    ry = -100
    rs = False
pygame.init()
screen = pygame.display.set_mode((500,500))
x = 225
y = 450
dx = 1
hp = 3


rx = -100
ry = -100
rs = False

pygame.init()



num_rect = random.randint(3, 5)

rect = [Rect(random.randint(1, 449,), 50, random.randint(5, 10,), 50, 50, True) for i in range(num_rect)]
bullets = [Rect(-100, -100, 15, 25, 25, False) for i in range(num_rect)]
 
while True:
    
    
    screen.fill((225, 225 , 225))
    hp_text = font.render(str(hp), True, (225, 255, 255))
    screen.blit(hp_text, (450, 10))
    for event in pygame.event.get():
        pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x < 450:
        x += 3
    if keys[pygame.K_a] and x >0:
        x -= 3
    if keys[pygame.K_SPACE] and rs == False:
        rx = x + 50 // 4
        ry = y
        rs = True
        
    


    if ry <= 0:
        kill_roket()
        
        
    
        
    if rs:
        pygame.draw.rect(screen, (255, 255, 0,), (rx, ry, 25, 25,))
        ry -= 12
        
        
    if hp <=0:
        break
        
    for i in range(len(rect)):
        if rect[i].x > x and rect[i].x < x + 50 and bullets[i].s == False:
            bullets[i].x = rect[i].x + rect[i].width // 4
            bullets[i].y = rect[i].y
            bullets[i].s = True
        
        if bullets[i].s:
            bullets[i].y += bullets[i].dx
            pygame.draw.rect(screen, (0, 255, 255), (bullets[i].x,bullets[i].y,bullets[i].width, bullets[i].height))
        if bullets[i].y >=500:
            bullets[i].die()

        if (x < bullets[i].x < x + 50 or x <  bullets[i].x + bullets[i].width < + 50) and bullets[i].y + bullets[i].height >= y:
            bullets[i].die()
            hp -= 1
        if rect[i].s:
            rect[i].x += rect[i].dx
            pygame.draw.rect(screen,(255, 255, 255), (rect[i].x, rect[i].y, 50, 50))
        if rect[i].x >= 450 or rect[i].x <= 0:
            rect[i].dx = -rect[i].dx
        if (rx >= rect[i].x and rx <= rect[i].width or rx + 25 <= rect[i].x + rect [i].width and rx + 25 >=rect[i].x) and \
           ry <=rect[i].y + rect[i].height:
           kill_roket()
           rect[i].die()
        
        
    pygame.draw.rect(screen,(50, 200, 50), (x, y, 50, 50))
    pygame.display.update()
    pygame.time.delay(8)
font = pygame.font.Font(None, 60)
text = font.render("GAME OVER!", True, (255, 255, 255))
screen.blit(text, (100, 200))
pygame.display.update()
    
    
    
    
      