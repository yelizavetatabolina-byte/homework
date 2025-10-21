import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Падающие шары")
screen_width = 600
screen_height = 400

egg_image = pygame.image.load("egg.png").convert()
key_sound = pygame.mixer.Sound("chicken-man.wav")
background_eggs = pygame.image.load("eggs.jpg")
basket_image = pygame.image.load("basket.png").convert()

basket_image = pygame.transform.scale(basket_image, (70, 70))
egg_image = pygame.transform.scale(egg_image, (75, 45))

basket_image.set_colorkey((255, 255, 255)) 
egg_image.set_colorkey((255, 255, 255)) 

background_eggs = pygame.transform.scale(background_eggs, (screen_width, screen_height))

font = pygame.font.SysFont(None, 36)  

running = True
clock = pygame.time.Clock()

balls = [] 
spawn_interval = 2000  
last_spawn_time = 0

score = 0
missed = 0

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    basket_x, basket_y = pygame.mouse.get_pos()
    if current_time - last_spawn_time > spawn_interval:
        x = random.randint(20, 580) 
        y = 0  
        speed_x =  random.choice([-2, -1, 0, 1, 2])
        balls.append([x, y, speed_x])
        last_spawn_time = current_time

    new_balls = []
    for ball in balls:
        x, y, speed_x = ball
        ball[1] += 2
        ball[0] += ball[2]
        dx = basket_x - x
        dy = basket_y - y
        distance = (dx**2 + dy**2)**0.5
        if distance < 30:  
            score += 1
            key_sound.play()  
        elif y > 400:  
            missed += 1
            if missed >= 3:
                print("Вы проиграли! Пропущено 3 шара")
                running = False
        else:
            new_balls.append(ball) 
    
    balls = new_balls
    screen.blit(background_eggs, (0, 0))
    for ball in balls:
        x, y, speed_x = ball
        screen.blit(egg_image, (x - 37, y - 22))
    
    screen.blit(basket_image, (basket_x - 35, basket_y - 35))
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    missed_text = font.render(f"Пропущено: {missed}/3", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()