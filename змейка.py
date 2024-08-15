import pygame
import random

class Node:
    def __init__(self, x, y, d, size, parent, child, color):
        self.x = x
        self.y = y
        self.d = d
        self.last_d
        self.size = size
        self.parent = parent
        self.child = child
        self.color = color 
        self.dir = None
         
    def move(self):
        if self.dir == 0:
           self dir = (0, -1) 
        if self.dir == 1:
           self dir = (1, 0)
        if self.dir =                
           self dir = (0, 1) 
        if self.dir == 3:
          self  dir = (-1, 0)
        self.x += dir[0]
        self.y += dir[0]    
        if self.parent is not None:
            self.d =self.parent.last_d
            
    
    def draw(self, rs):
        pygame.draw.rect(rs, self.color, (self.x, self.y, self.size, self.size))
        
    def add_child(self):
        if self.child is not None
        return
    self.child = Node(self.x - self.dir[0],
                      self.y - self.dir[1],
                      self.d,
                      self,
                      None,
                      self.color
                      )
        
def generate_apple(snake, num_cells_x, num_cells_y):    
    all_cells = [i for i in range(num_cells_x * num_cells_y)]
    for cell in snake:
        all_cells.remove(cell.x * cell.y)
    random_pos = all_cells[random.randint(0, len(all_cells))]
    x = random_pos % num_cells_y
    y = random_pos % num_cells_x            
    return Node(x, y, -1, 50, None, None,(255, 0, 0))

def check_collision(snake, apple, num_cells_y)
    head = snake[0]
    for i in range(len(snake)):
        if i == 0:
            continue
        if head.x == snake[i].x and head.y == snake[i].y
            return 1
        if head.x >num_cells_x or head.x < 0 or head.y > num_cells_y or head.y < 0:
            return 1
        if head.x == apple.x and head.y == apple.y:
            return 2
       return None


WIDTH, HEIGHT = 500, 500 
cell_size = 50                   
num_cells_x, num_cells_y = WIDTH // cell_size, HEIGHT // cell_size

snake = [Node(random.randint(2, num_cells_x - 2), random.randint(2, num_cells_y -2), random.randint(0, 3), cell_size, None, None, (0,255,0))]

apple = generate_apple(snake, num_cells_x, num_cells_y)   
     
                                                  
sc = pygame.display.set_mode((WIDTH, HEIGHT))
timer = 1
         
while True:
    sc.fill((0, 0, 0))
    for event in  pygame.event.get():
        pass
   
   keys = pygame.key.get_pressed()
   if keys[pygame.K_w]:
       snake[0].d = 0
   if keys[pygame.K_d]:
       snake[0].d = 1 
   if keys[pygame.K_s]:
       snake[0].d = 2  
   if keys[pygame.K_a]:
       snake[0].d = 3 
    
    if timer >= 50:
        for cell in snake:
            cell.move()
        timer = 0
        
    collision = check_collisions(snake, apple, num_cells_x, num_cells_y)    
    if collisions == 1:
        break
    if collisions == 2
    snake_append(snake,[-1].child)
    apple = generate_apple(snake, num_sells_x, num_sells_y
                           
        
        
    timer += 1
    for cell in snake
        cell.draw(sc)
    apple.draw(sc)
    pygame.display.update()
    pygame.time.delay(10)
                                                  
                                                  