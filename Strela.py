import pygame
import math 
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Стрельба из лука")

background_luk = pygame.image.load("polyanka.jpg")
background_luk = pygame.transform.scale(background_luk, (600, 400))
luk_image = pygame.image.load("luk.jpg")
luk_image = pygame.transform.scale(luk_image, (200, 200))
strela_image = pygame.image.load("strela.jpg")
strela_image = pygame.transform.scale(strela_image, (80, 50))
mishen_image = pygame.image.load("misheni.png")
mishen_image = pygame.transform.scale(mishen_image, (80, 80))

mishen_image.set_colorkey((255, 255, 255)) 
luk_image.set_colorkey((255, 255, 255))
strela_image.set_colorkey((255, 255, 255)) 

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1) 

score_sound = pygame.mixer.Sound("babach.wav")  

start_x, start_y = 80, 220
x, y = start_x, start_y
radius = 15

mishen1_x, mishen1_y = 500, 200
mishen1_speed = 1
mishen1_direction = 1
mishen2_x, mishen2_y = 400, 100
mishen2_speed = 1.5
mishen2_direction = -1

vx, vy = 0, 0
gravity = 0.5
power = 12
angle = 45
bounce_loss = 0.7
on_ground = True

font = pygame.font.Font(None, 24)

scored_flag = False
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                angle = min(angle + 5, 80)
            elif event.key == pygame.K_DOWN:angle = max(angle - 5, 10) 
            elif event.key == pygame.K_w:
                power = min(power + 1, 25)
            elif event.key == pygame.K_s:
                power = max(power - 1, 5)
            elif event.key == pygame.K_SPACE and on_ground:
                rad = math.radians(angle)
                vx = power * math.cos(rad)
                vy = -power * math.sin(rad)
                on_ground = False

    mishen1_y += mishen1_speed * mishen1_direction
    if mishen1_y >= 350 or mishen1_y <= 50:
        mishen1_direction *= -1
        
    mishen2_y += mishen2_speed * mishen2_direction
    if mishen2_y >= 350 or mishen2_y <= 50:
        mishen2_direction *= -1
        
    if not on_ground:
        vy += gravity
        x += vx
        y += vy
        
        if y + radius >= 400:
            y = 400 - radius
            vy = -vy * bounce_loss
            vx *= bounce_loss
            if abs(vy) < 1 and abs(vx) < 1:
                x, y = start_x, start_y
                vx, vy = 0, 0
                on_ground = True
                scored_flag = False
                
    if not on_ground and not scored_flag:
        distance = math.sqrt((x - mishen1_x)**2 + (y - mishen1_y)**2)
        if distance < 30:
            scored_flag = True
            score += 1
            score_sound.play()

        distance2 = math.sqrt((x - mishen2_x)**2 + (y - mishen2_y)**2)
        if distance2 < 30:
            scored_flag = True
            score += 1
            score_sound.play()

    screen.blit(background_luk, (0, 0))
    screen.blit(luk_image, (5,130))

    if on_ground:
        points = []
        rad = math.radians(angle)
        temp_vx = power * math.cos(rad)
        temp_vy = -power * math.sin(rad)
        temp_x, temp_y = start_x, start_y
        for i in range(60): 
            temp_vy += gravity
            temp_x += temp_vx
            temp_y += temp_vy
            if temp_y + radius >= 400:
                break
            points.append((int(temp_x), int(temp_y)))
        if len(points) > 1:
            pygame.draw.lines(screen, (0, 0, 0), False, points, 2)
            
    screen.blit(mishen_image, (int(mishen1_x - 15), int(mishen1_y - 15)))
    screen.blit(mishen_image, (int(mishen2_x - 15), int(mishen2_y - 15)))

    screen.blit(strela_image, (int(x - radius), int(y - radius)))

    text_angle = font.render(f"Угол: {angle}°", True, (255, 0, 0))
    text_power = font.render(f"Сила: {power}", True, (255, 0, 0))
    text_score = font.render(f"Счёт: {score}", True, (255, 0, 0))
    screen.blit(text_angle, (10, 10))
    screen.blit(text_power, (10, 30))
    screen.blit(text_score, (10, 50))

    if scored_flag:
        hit_text = font.render("ПОПАДАНИЕ!", True, (0, 255, 0))
        screen.blit(hit_text, (250, 50))

    pygame.display.flip()
    pygame.time.delay(20)
    
pygame.quit()