import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Солнечная система")
WIDTH, HEIGHT = 800, 600
cx = WIDTH // 2
cy = HEIGHT // 2   
FPS = 60
clock = pygame.time.Clock()
pygame.mixer.music.load("cosmos.mp3")           
pygame.mixer.music.play(-1)

class Planet:
    def __init__(self, screen, radius, orbit_radius, color=None, speed=0, angle=0, image_path=None, sputnic=None):
        self.screen = screen
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.color = color
        self.speed = speed
        self.angle = angle
        self.x = 0
        self.y = 0
        self.image = None
        self.sputnic = sputnic
        if image_path:
            self.image = pygame.image.load(image_path).convert()
            self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
            self.image.set_colorkey((255, 255, 255))

    def update(self, dt):
        self.angle += self.speed * dt
        
        if self.sputnic:
            self.x = self.sputnic.x + self.orbit_radius * math.cos(self.angle)
            self.y = self.sputnic.y + self.orbit_radius * math.sin(self.angle)
        else:
            self.x = cx + self.orbit_radius * math.cos(self.angle)
            self.y = cy + self.orbit_radius * math.sin(self.angle)

    def draw(self):
        if self.image:
            self.screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
        else:
            pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)


class Comet:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("comet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 15))
        self.reset()
    
    def reset(self):
        self.x = random.randint(-100, WIDTH + 100)
        self.y = random.randint(-100, -50)
        self.speed = random.uniform(100, 200)
    
    def update(self, dt):
        self.x += self.speed * dt
        self.y += self.speed * dt
        
        if self.x > WIDTH + 100 or self.y > HEIGHT + 100:
            self.reset()
    
    def draw(self):
        self.screen.blit(self.image, (int(self.x), int(self.y)))

class Astronaut:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("astronaut.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.step = 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.step
        if keys[pygame.K_DOWN]:
            self.y += self.step
        if keys[pygame.K_LEFT]:
            self.x -= self.step
        if keys[pygame.K_RIGHT]:
            self.x += self.step
        
        self.x = max(20, min(WIDTH - 20, self.x))
        self.y = max(30, min(HEIGHT - 30, self.y))
    
    def draw(self):
        self.screen.blit(self.image, (int(self.x - 20), int(self.y - 30)))     

sun_color = (255, 200, 0)
sun_radius = 20

earth = Planet(screen, radius=20, orbit_radius=130, speed=1, image_path="earth.png")
moon = Planet(screen, radius=5, orbit_radius=40, speed=3, color=(200, 200, 200), sputnic=earth)
venera = Planet(screen, radius=14, orbit_radius=100, speed=1.3, image_path="venera.png")
neptun = Planet(screen, radius=30, orbit_radius=280, speed=0.3, image_path="neptun.png")
pluton = Planet(screen, radius=4, orbit_radius=300, speed=0.2, image_path="pluton.png")
saturn = Planet(screen, radius=40, orbit_radius=210, speed=0.5, image_path="saturn.png")
upiter = Planet(screen, radius=45, orbit_radius=180, speed=0.6, image_path="upiter.png")
merkyrii = Planet(screen, radius=4, orbit_radius=60, speed=1.6, image_path="merkyrii.png")
uran = Planet(screen, radius=35, orbit_radius=240, speed=0.4, image_path="uran.png")
mars = Planet(screen, radius=6, orbit_radius=150, color=(255, 100, 80), speed=0.8, image_path="mars.png")

planets = [earth, moon, mars, venera, uran, pluton, neptun, saturn, upiter, merkyrii]
comets = [Comet(screen) for _ in range(5)]
astronaut = Astronaut(screen)

running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            cx = WIDTH // 2
            cy = HEIGHT // 2

    for planet in planets:
        planet.update(dt)
    for comet in comets:
        comet.update(dt)
    astronaut.update()
    screen.fill((0, 0, 20))
    for comet in comets:
        comet.draw()
    
    pygame.draw.circle(screen, sun_color, (cx, cy), sun_radius)
    
    for planet in planets:
        planet.draw()
    astronaut.draw()    
    pygame.display.flip()

pygame.quit()