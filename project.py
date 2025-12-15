import pygame
import math 
import random

def init_game():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("Стрельба из лука")
    return width, height, screen

def load_images(width, height):
    background_orig = pygame.image.load("polyanka.jpg")
    background = pygame.transform.scale(background_orig, (width * 2, height))
    luk = pygame.transform.scale(pygame.image.load("luk.png"), (200, 200))
    strela = pygame.transform.scale(pygame.image.load("strela.png"), (70, 50))
    mishen = pygame.transform.scale(pygame.image.load("misheni.png"), (90, 90))
    pregrada = pygame.transform.scale(pygame.image.load("peny.png"), (80, 60))
    
    for img in [mishen, luk, strela, pregrada]:
        img.set_colorkey((255, 255, 255))
    
    return background, luk, strela, mishen, pregrada

def create_pregrada(width, height, pregrada):
    return [width + random.randint(0, 200), height - pregrada.get_height() - random.randint(10, 50)]

def update_pregradas(pregradas, width, height, pregrada, pregrada_timer, bg_speed):
    pregrada_timer += 1
    if pregrada_timer >= 180:
        pregradas.append(create_pregrada(width, height, pregrada))
        pregrada_timer = 0
    
    pregradas[:] = [ [p[0] + bg_speed, p[1]] for p in pregradas if p[0] > -100 ]
    
    return pregrada_timer

def check_stolknoveniy(luk_x, luk_y, luk, pregradas, pregrada, last_collision_time):
    luk_rect = pygame.Rect(luk_x - luk.get_width()//4, luk_y - luk.get_height()//4, 
                          luk.get_width()//2, luk.get_height()//2)
    current_time = pygame.time.get_ticks()
    
    for p in pregradas:
        pregrada_rect = pygame.Rect(p[0] + 15, p[1] + 10, 
                                   pregrada.get_width() - 30, pregrada.get_height() - 20)
        if luk_rect.colliderect(pregrada_rect) and current_time - last_collision_time > 500:
            return True, current_time
    return False, last_collision_time

def update_physics(luk_y, luk_y_speed, luk_gravity, height, luk):
    luk_y_speed += luk_gravity
    luk_y += luk_y_speed
    
    if luk_y + luk.get_height()//2 >= height:
        luk_y = height - luk.get_height()//2
        luk_y_speed = 0
    elif luk_y - luk.get_height()//2 <= 0:
        luk_y = luk.get_height()//2
        luk_y_speed = 0
    
    return luk_y, luk_y_speed

def update_strela(x, y, vx, vy, gravity, energy_lose, height, radius, start_x, start_y):
    vy += gravity
    x += vx
    y += vy
    
    if y + radius >= height:
        y = height - radius
        vy = -vy * energy_lose
        vx *= energy_lose
        if abs(vy) < 1 and abs(vx) < 1:
            return start_x, start_y, 0, 0, True
    
    return x, y, vx, vy, False

def check_hits(x, y, mishen1_x, mishen1_y, mishen2_x, mishen2_y):
    distance1 = math.sqrt((x - mishen1_x)**2 + (y - mishen1_y)**2)
    distance2 = math.sqrt((x - mishen2_x)**2 + (y - mishen2_y)**2)
    return distance1 < 25 or distance2 < 25

def draw_trajectory(screen, start_x, start_y, angle, power, gravity, height, radius):
    points = []
    rad = math.radians(angle)
    temp_vx = power * math.cos(rad)
    temp_vy = -power * math.sin(rad)
    temp_x, temp_y = start_x, start_y
    
    for i in range(60):
        temp_vy += gravity
        temp_x += temp_vx
        temp_y += temp_vy
        if temp_y + radius >= height:
            break
        points.append((int(temp_x), int(temp_y)))
    
    if len(points) > 1:
        pygame.draw.lines(screen, (0, 0, 0), False, points, 2)

def main():
    width, height, screen = init_game()
    background, luk, strela, mishen, pregrada = load_images(width, height)
    font = pygame.font.Font(None, 36)
    
    luk_x, luk_y = 50, height - 150
    luk_gravity, luk_y_speed = 2, 0
    
    start_x = luk_x + luk.get_width()//2 - 20
    start_y = luk_y - 15
    
    x, y, vx, vy = start_x, start_y, 0, 0
    radius, power, angle = 15, 12, 45
    gravity, energy_lose = 0.5, 0.7
    on_ground, scored_flag = True, False
    
    mishen1_x = width * 0.75
    mishen1_y = height * 0.3
    mishen2_x = width * 0.85
    mishen2_y = height * 0.2
    mishen1_speed, mishen2_speed = 1, 1.5
    mishen1_dir, mishen2_dir = 1, -1
    
    pregradas = []
    pregrada_timer = 0
    pregrada_touches = 0
    last_collision_time = 0
    
    bg_x = 0
    bg_speed = 0
    
    target_hits = 0
    game_over = False
    game_won = False
    
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1) 
    score_sound = pygame.mixer.Sound("babach.wav")
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        dt = clock.tick(60) / 1000.0
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                background, luk, strela, mishen, pregrada = load_images(width, height)
                mishen1_x = width * 0.75
                mishen1_y = height * 0.3
                mishen2_x = width * 0.85
                mishen2_y = height * 0.2
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: angle = min(angle + 5, 80)
                elif event.key == pygame.K_s: angle = max(angle - 5, 10)
                elif event.key == pygame.K_d: power = min(power + 1, 25)
                elif event.key == pygame.K_a: power = max(power - 1, 5)
                elif event.key == pygame.K_z and on_ground:
                    rad = math.radians(angle)
                    vx, vy = power * math.cos(rad), -power * math.sin(rad)
                    on_ground = False
                elif event.key == pygame.K_UP: luk_y_speed = -20
        
        if not game_over and not game_won:
            bg_speed = 0
            if keys[pygame.K_LEFT]: 
                bg_speed = 5
                bg_x += bg_speed
                if bg_x >= width * 2:
                    bg_x = 0
                elif bg_x <= -width * 2:
                    bg_x = 0
            if keys[pygame.K_RIGHT]: 
                bg_speed = -5
                bg_x -= 5
                if bg_x >= width * 2:
                    bg_x = 0
                elif bg_x <= -width * 2:
                    bg_x = 0
            
            luk_y, luk_y_speed = update_physics(luk_y, luk_y_speed, luk_gravity, height, luk)
            
            start_x = luk_x + luk.get_width()//2 - 20
            start_y = luk_y - 15
            
            if on_ground: 
                x, y = start_x, start_y
            
            mishen1_y += mishen1_speed * mishen1_dir
            if mishen1_y >= height - 50 or mishen1_y <= 50: 
                mishen1_dir *= -1
            mishen2_y += mishen2_speed * mishen2_dir
            if mishen2_y >= height - 50 or mishen2_y <= 50: 
                mishen2_dir *= -1
            
            pregrada_timer = update_pregradas(pregradas, width, height, pregrada, pregrada_timer, bg_speed)
            
            stolknovenie, last_collision_time = check_stolknoveniy(luk_x, luk_y, luk, pregradas, pregrada, last_collision_time)
            if stolknovenie:
                pregrada_touches += 1
                luk_y_speed = -10
                if pregrada_touches >= 1: 
                    game_over = True
            
            if not on_ground:
                x, y, vx, vy, landed = update_strela(x, y, vx, vy, gravity, energy_lose, height, radius, start_x, start_y)
                if landed: 
                    on_ground, scored_flag = True, False
                    x, y = start_x, start_y
                
                if not scored_flag and check_hits(x, y, mishen1_x, mishen1_y, mishen2_x, mishen2_y):
                    scored_flag = True
                    target_hits += 1
                    score_sound.play()
                    
                    if target_hits >= 5: 
                        game_won = True
        
        screen.fill((100, 200, 100))
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x - width * 2, 0))
        screen.blit(background, (bg_x + width * 2, 0))
        
        for p in pregradas: 
            screen.blit(pregrada, (p[0], p[1]))
        
        screen.blit(luk, (luk_x - luk.get_width()//2, luk_y - luk.get_height()//2))
        
        if on_ground: 
            draw_trajectory(screen, start_x, start_y, angle, power, gravity, height, radius)
            screen.blit(strela, (start_x - strela.get_width()//2, start_y - strela.get_height()//2))
        else: 
            screen.blit(strela, (x - strela.get_width()//2, y - strela.get_height()//2))
        
        screen.blit(mishen, (mishen1_x - mishen.get_width()//2, mishen1_y - mishen.get_height()//2))
        screen.blit(mishen, (mishen2_x - mishen.get_width()//2, mishen2_y - mishen.get_height()//2))
        
        texts = [
            font.render(f"Угол: {angle}°", True, (255, 0, 0)),
            font.render(f"Сила: {power}", True, (255, 0, 0)),
            font.render(f"Попадания: {target_hits}/5", True, (255, 0, 0)),
            font.render(f"Касания: {pregrada_touches}/1", True, (255, 0, 0))
        ]
        for i in range(len(texts)):
            text = texts[i]
            screen.blit(text, (10, 10 + i * 30))
        
        if game_won: 
            screen.blit(font.render("ПОБЕДА! Вы выиграли!", True, (0, 255, 0)), 
                       (width//2 - 150, height//2 - 50))   
        if game_over: 
            screen.blit(font.render("ПРОИГРЫШ! Вы проиграли!", True, (255, 0, 0)), 
                       (width//2 - 150, height//2 - 50))
        
        pygame.display.flip()
    
    pygame.quit()

main()
