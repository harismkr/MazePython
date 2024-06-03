import pygame
import time

pygame.init()
screen=pygame.display.set_mode((1500, 800))
done = False
x=90
y=90

ts1 = time.time()
ts2 = time.time()
tol1 = 0
tol2 = 0
clock=pygame.time.Clock()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 4
    if pressed[pygame.K_DOWN]: y += 4
    if pressed[pygame.K_LEFT]: x -= 4
    if pressed[pygame.K_RIGHT]: x += 4

    IMAGE = pygame.image.load('img.png').convert()
    pl1 = IMAGE.get_rect()
    pl1.center = (x, y)
    screen.blit(IMAGE, pl1)

    Font = pygame.font.SysFont("comicsansms", 170, True, True)
    Title = Font.render("Maze Game", True, (100, 100, 100))
    screen.blit(Title, (250, 0))

    Font = pygame.font.SysFont("comicsansms", 50, True, True)
    Title = Font.render("Start", True, (100, 100, 100))
    screen.blit(Title, (20, 0))

    Font = pygame.font.SysFont("comicsansms", 50, True, True)
    Title = Font.render("End", True, (100, 100, 100))
    screen.blit(Title, (110, 480))

    wl1 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(0, 0, 2000, 20))
    wl2 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(0, 0, 20, 1000))
    wl3 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(1480, 0, 20, 800))
    wl4 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(0, 780, 1500, 20))
    wl5 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(0, 400, 800, 20))
    wl6 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(1000, 400, 800, 20))
    wl7 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(100, 550, 100, 100))
    wl8 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(600, 400, 20, 300))
    wl9 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(300, 100, 20, 300))
    wl10 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(550, 20, 20, 300))
    wl11 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(1000, 20, 20, 150))
    wl12 = pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(1000, 250, 20, 150))

    if pl1.colliderect(wl1) or pl1.colliderect(wl2) or pl1.colliderect(wl3) or pl1.colliderect(wl4) or pl1.colliderect(
            wl5) or pl1.colliderect(wl6) or pl1.colliderect(wl8) or pl1.colliderect(wl9) or pl1.colliderect(
            wl10) or pl1.colliderect(wl11) or pl1.colliderect(wl12):
        if pressed[pygame.K_UP]: y += 4
        if pressed[pygame.K_LEFT]: x += 4
        if pressed[pygame.K_RIGHT]: x -= 4
        if pressed[pygame.K_DOWN]: y -= 4
        if pl1.colliderect(wl7):
            x = 30
            y = 30

    if pl1.colliderect(wl7):
        x = 30
        y = 30
        te1 = time.time()
        tol1 = round(te1 - ts1, 2)
        ts1 = time.time()

    Font1 = pygame.font.SysFont("comicsansms", 20, True, True)
    Time1 = Font1.render("Time to finish:" + str(tol1), True, (0, 0, 255))
    screen.blit(Time1, (50, 650))

    pygame.display.flip()
    clock.tick(60)
















