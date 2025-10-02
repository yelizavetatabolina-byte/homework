import pygame
pygame.init()
font = pygame.font.SysFont(None, 40)

screen = pygame.display.set_mode((625, 800))
pygame.display.set_caption("Единорожик")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (0, 365, 625, 450))  
    pygame.draw.circle(screen, (255,221,85), (584, 75), 118) 
    pygame.draw.rect(screen, (230,230,230), (86, 450, 42, 125))
    
    pygame.draw.ellipse(screen, (0,128,1), (18,325,174,140))
    pygame.draw.ellipse(screen, (0,128,1), (-50,230,310,145))
    pygame.draw.ellipse(screen, (0,128,1), (18,105,174,200))
    
    pygame.draw.ellipse(screen, (254,204,164), (200,290,45,39))
    pygame.draw.ellipse(screen, (254,204,164), (-20,290,45,39))
    pygame.draw.ellipse(screen, (254,204,164), (120,140,45,39))
    pygame.draw.circle(screen, (254,204,164), (148, 438), 22)

    
    pygame.draw.ellipse(screen, (233,175,174), (192,612,72,18))
    pygame.draw.ellipse(screen, (233,175,174), (251,567,45,18))
    pygame.draw.ellipse(screen, (233,198,176), (230,578,50,30))
    pygame.draw.ellipse(screen, (229,255,128), (250,640,64,21))
    pygame.draw.ellipse(screen, (233,198,176), (212,618,83,25))
    pygame.draw.ellipse(screen, (255,238,169), (215,601,65,27))
    pygame.draw.ellipse(screen, (255,238,169), (210,634,46,16))
    pygame.draw.ellipse(screen, (229,255,128), (205,618,50,17))
    pygame.draw.ellipse(screen, (229,255,128), (235,662,55,17))
    pygame.draw.ellipse(screen, (247,215,228), (212,643,75,24))
    pygame.draw.ellipse(screen, (175,233,221), (199,649,58,17))
    pygame.draw.ellipse(screen, (247,215,228), (232,657,50,15))
    pygame.draw.ellipse(screen, (175,233,221), (253,655,46,17))
    pygame.draw.ellipse(screen, (175,233,221), (198,638,35,12))
    pygame.draw.ellipse(screen, (229,255,128), (180,680,70,21))
    pygame.draw.ellipse(screen, (233,198,176), (201,669,46,16))
    pygame.draw.ellipse(screen, (255,238,169), (231,678,46,16))
    pygame.draw.ellipse(screen, (220,175,232), (176,660,72,17))
    pygame.draw.ellipse(screen, (247,215,228), (209,685,75,24))
    pygame.draw.ellipse(screen, (175,233,221), (255,682,40,12))
    pygame.draw.ellipse(screen, (175,233,221), (242,694,58,17))
    pygame.draw.ellipse(screen, (247,215,228), (211,703,60,15))
    pygame.draw.ellipse(screen, (175,233,221), (253,655,58,17))
    
    
    pygame.draw.ellipse(screen, (233,175,174), (447,433,38,21))
    pygame.draw.ellipse(screen, (233,198,176), (430,455,47,21))
    pygame.draw.ellipse(screen, (233,175,174), (421,448,45,15))
    pygame.draw.ellipse(screen, (233,198,176), (400,459,50,30))
    pygame.draw.ellipse(screen, (229,255,128), (420,518,64,21))
    pygame.draw.ellipse(screen, (233,198,176), (405,498,60,25))
    pygame.draw.ellipse(screen, (255,238,169), (385,482,65,27))
    pygame.draw.ellipse(screen, (255,238,169), (387,515,46,16))
    pygame.draw.ellipse(screen, (229,255,128), (375,502,48,17))
    pygame.draw.ellipse(screen, (247,215,228), (389,525,75,24))
    pygame.draw.ellipse(screen, (175,233,221), (369,530,58,17))
    pygame.draw.ellipse(screen, (247,215,228), (402,538,50,15))
    pygame.draw.ellipse(screen, (175,233,221), (430,534,46,17))
    pygame.draw.ellipse(screen, (175,233,221), (190,697,50,19))
    pygame.draw.ellipse(screen, (220,175,232), (247,707,69,17))
    
    pygame.draw.ellipse(screen, (255,255,255), (270,540,259,120))
    pygame.draw.ellipse(screen, (255,255,255), (470,460,100,40))
    pygame.draw.rect(screen, (255,255,255), (425, 490, 90, 110))
    pygame.draw.ellipse(screen, (255,255,255), (430,443,100,55))
    pygame.draw.ellipse(screen, (229,129,255), (490,460,22,19))
    pygame.draw.ellipse(screen, (0,0,0), (500,465,9,8))

    pygame.draw.rect(screen, (255,255,255), (429, 611, 22, 133))
    pygame.draw.rect(screen, (255,255,255), (485, 580, 18, 133))
    pygame.draw.rect(screen, (255,255,255), (342, 599, 23, 125))

    pygame.draw.ellipse(screen, (233,175,174), (447,433,38,21))
    pygame.draw.ellipse(screen, (233,198,176), (430,455,47,21))
    pygame.draw.ellipse(screen, (233,175,174), (421,448,45,15))
    pygame.draw.ellipse(screen, (233,198,176), (400,459,50,30))
    pygame.draw.ellipse(screen, (229,255,128), (420,518,64,21))
    pygame.draw.ellipse(screen, (233,198,176), (405,498,60,25))
    pygame.draw.ellipse(screen, (255,238,169), (385,482,65,27))
    pygame.draw.ellipse(screen, (255,238,169), (387,515,46,16))
    pygame.draw.ellipse(screen, (229,255,128), (375,502,48,17))
    
    pygame.draw.ellipse(screen, (247,215,228), (389,525,75,24))
    pygame.draw.ellipse(screen, (175,233,221), (369,530,58,17))
    pygame.draw.ellipse(screen, (247,215,228), (402,538,50,15))
    pygame.draw.ellipse(screen, (175,233,221), (430,534,46,17))
    pygame.draw.ellipse(screen, (175,233,221), (370,520,35,12))
    pygame.draw.ellipse(screen, (220,175,232), (349,538,69,17))
    
    pygame.draw.line(screen, (255, 255, 255), (495, 462), (503, 466), 5) 
    pygame.draw.polygon(screen, (233, 175, 174), [(475, 444), (495, 447), (499,355)])



    
    pygame.draw.rect(screen, (255,255,255), (292, 610, 19, 125))
    pygame.draw.rect(screen, (255,255,255), (485, 580, 18, 125))
    mx, my = pygame.mouse.get_pos()
    text = font.render(f"x: {mx}, y: {my}", True, (0, 0, 0))
    screen.blit(text, (10, 10))


    pygame.display.flip()
    

pygame.quit()