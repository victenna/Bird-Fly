import pygame
import math,random,time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1400
screen_height = 800

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

#back ground images
bground_img1=pygame.image.load('bground0.png')
bground_img2=pygame.image.load('bground1.png')

# Load bird images
bird_images = []
for i in range(10):
    #bird_img = pygame.image.load(f"bird{i}.png")
    bird_img = pygame.image.load(f"bird{i}.png")
    #bird_img = pygame.transform.scale(bird_img, (100, 100))
    bird_img = pygame.transform.scale(bird_img, (50,50))
    bird_width,bird_height=bird_img.get_size()
    bird_images.append(bird_img)

# Load gunman image
gunman_img = pygame.image.load("gun_man.png")
gunman_img = pygame.transform.scale(gunman_img, (200, 200))

# Load bullet image
bullet_img = pygame.image.load("bullet2.png")
bullet_img = pygame.transform.scale(bullet_img, (20, 20))
bullet_width,bullet_height=bullet_img.get_size()

# Bird properties
bird_x = 15
bird_y = screen_height // 2
bird_y_speed = 0

# Gunman properties
gunman_x = 50
gunman_y = screen_height - 200

# Bullet properties
bullet_x = gunman_x + 155  # Adjust the bullet starting position
bullet_y = gunman_y +45 # Adjust the bullet starting position
bullet_speed = 5
bullet_angle = math.radians(25)  # Angle in radians
bullet_speed = 40
bullet_active = False

#Set Start Button
button=pygame.image.load('start.png')
button_rect=button.get_rect(center=(700,150))
screen.blit(button,button_rect)

#set game start
game_started=False
q = 0
s=0
Score=0

# Set up font
font = pygame.font.Font(None, 60)

# Initialize variables
start_time = time.time()

# Game variables
game_over = False

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    q = q + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:# and event.button == 1:
            if button_rect.collidepoint(event.pos):
                game_started = True
    
    #Screen fill
    if game_started==False:
        screen.blit(bground_img1,(0,0))
                
    screen.blit(button,button_rect)
    q1 = q % 10  # Using the number of bird images
    keys=pygame.key.get_pressed()

    if game_started:
        screen.blit(bground_img2,(0,0))
        screen.blit(bird_images[q1], (bird_x, bird_y))
        screen.blit(bullet_img, (bullet_x, bullet_y))
        current_time = time.time()
        runtime_seconds = int(current_time - start_time)
        text = font.render('Run Time in Sec='+str(runtime_seconds),True,'white')
        screen.blit(text,(100,150))
        
        if runtime_seconds>60:
            game_over = True
            game_started=False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bullet_active= True
        if bullet_active:
            bullet_x += bullet_speed * math.cos(bullet_angle)
            bullet_y -= bullet_speed * math.sin(bullet_angle)
            screen.blit(bullet_img, (bullet_x, bullet_y))

        if s==0 :
            # Bird movement
            bird_x += 15
            
            # Display the bird image
            if bird_x > screen_width - 100:
                bird_x = 0
            bird_rect=bird_img.get_rect().move(bird_x,bird_y)
            bullet_rect=bullet_img.get_rect().move(bullet_x,bullet_y)
            
            if bird_rect.colliderect(bullet_rect):
                s=1
                Score=Score+1
        if s==1:
                
            bullet_x=20000
            bird_y += 10  # Move the bird down by 20 pixels vertically
            #print('s=',s,'bird_y=',bird_y)
        if bird_y > screen_height: # If bird hits bottom of screen
            bullet_x = gunman_x + 155
            bullet_y = gunman_y + 45
            bird_x = 15
            bird_y = screen_height // 2+random.randint(-300,150)
            s=0
            bullet_active= False
        if bullet_x > screen_width or bullet_y < 0:
            bullet_active = False
            bullet_x = gunman_x + 155 
            bullet_y = gunman_y + 45
            screen.blit(bullet_img, (bullet_x, bullet_y))
   
    #Score
    score_text = font.render("score number= " + str(Score), True, 'white')
    screen.blit(score_text, (100, 100))
    
    # If the game is over, display "GAME OVER"
    if game_over==True:
        game_started==False
        game_over_text = font.render("GAME OVER", True, 'white')
        text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.fill('blue')
        screen.blit(game_over_text, text_rect)
        
        text = font.render('Run Time in Sec='+str(runtime_seconds),True,'white')
        screen.blit(text,(100,150))
        
        score_text = font.render("score number= " + str(Score), True, 'white')
        screen.blit(score_text, (100, 100))
    
    # Update the screen
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()