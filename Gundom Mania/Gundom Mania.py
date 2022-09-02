import time

import pygame
from pygame.locals import *

pygame.init()

WIDTH = 1000
HEIGHT = 1000

BLUE = 0, 100, 250
BLACK = 250, 250, 250

SCORE1 = 0
SCORE2 = 0

start = False

item = "pistol"

item2 = "pistol"

WIN1 = False

WIN2 = False

title = pygame.image.load("assets/title.png")
title = pygame.transform.scale(title, (WIDTH, HEIGHT))

sg_hitbox = pygame.Rect(WIDTH / 2 - 100, HEIGHT - 250, 200, 100)
sg_img = pygame.image.load("assets/button.png")
sg_img = pygame.transform.scale(sg_img, (200, 220))

x = 150
y = HEIGHT / 2 - 10

x2 = WIDTH - 150
y2 = HEIGHT / 2 - 10

outerspace = pygame.image.load("assets/outerspace.png")
outerspace = pygame.transform.scale(outerspace, (WIDTH, HEIGHT))

shoot = False

shoot2 = False

FPS = 60

caption = "Gundom Mania"

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(caption)

bullet = pygame.Rect(20, 20, 15, 10)

bullet2 = pygame.Rect(20, 20, 15, 10)

bullet_img = pygame.image.load("assets/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (15, 10))

bullet_img2 = pygame.image.load("assets/bullet2.png")
bullet_img2 = pygame.transform.scale(bullet_img2, (15, 10))

pistol = pygame.image.load("assets/pistol.png")
pistol = pygame.transform.scale(pistol, (150, 90))
pistol = pygame.transform.rotate(pygame.transform.scale(pistol, (150, 150)), 270)

pistol2 = pygame.image.load("assets/pistol.png")
pistol2 = pygame.transform.scale(pistol, (150, 90))
pistol2 = pygame.transform.rotate(pygame.transform.scale(pistol2, (150, 150)), 180)

crs = pygame.Rect(10, 10, 10, 10)

player = pistol.get_rect()

player2 = pistol2.get_rect()

def draw_on_window():
    WINDOW.blit(outerspace, (0, 0))
    if shoot == True:
        item = "pistol"
    else:
        item = " "
        
    if shoot2 == True:
        item2 = "pistol"
    else:
        item2 = " "
        
    if item == "pistol":
        WINDOW.blit(bullet_img, (bullet.x, bullet.y + 10))
        
    if item2 == "pistol":
       WINDOW.blit(bullet_img2, (bullet2.x, bullet2.y))

    WINDOW.blit(pistol, (x - 50, y - 60))
    WINDOW.blit(pistol2, (x2 - 50, y2 - 60))
        
    MTS(" ", BLACK)
        
    pygame.display.update()
    
def home_screen():
    WINDOW.blit(title, (0, 0))
    WINDOW.blit(sg_img, (WIDTH / 2 - 100, HEIGHT - 302))
    pygame.display.update()
    
def score_system():
    global SCORE1
    global SCORE2
    
    MTS(" ", BLACK)
    
    if bullet.colliderect(player2):
        SCORE1 += 1
        bullet.x = x
        
    if bullet2.colliderect(player):
        SCORE2 += 1
        bullet2.x = x2
        shoot2 = False
        
    MTS(" ", BLACK)
        
font = pygame.font.SysFont(None, 25)

def WIN_OR_LOSE():
    if SCORE1 > 10:
        WIN1 = True
    else:
        WIN1 = False
        
    if SCORE2 > 10:
        WIN2 = True
    else:
        WIN2 = False
        
    MTS(" ", BLACK)
        
def MTS(msg, color):
    screen_text = font.render(str(SCORE1), True, color)
    WINDOW.blit(screen_text, (215, 50))
    screen_text = font.render("SCORE OF PLAYER 1: ", True, color)
    WINDOW.blit(screen_text, (30, 50))
    screen_text = font.render(str(SCORE2), True, color)
    WINDOW.blit(screen_text, (WIDTH - 30, 50))
    screen_text = font.render("SCORE OF PLAYER 2: ", True, color)
    WINDOW.blit(screen_text, (WIDTH - 215, 50))
    pygame.display.update()
    
big_font = pygame.font.SysFont(None, 75)
    
def DMTS(msg, color):
    
    screen_text = big_font.render("THE WINNER IS: ", True, color)
    WINDOW.blit(screen_text, ((WIDTH / 2) - 325, 150))
    
    if SCORE1 > 10:
        screen_text = big_font.render("PLAYER 1", True, color)
        WINDOW.blit(screen_text, (WIDTH / 2 + 100, 150))
        
    if SCORE2 > 10:
        screen_text = big_font.render("PLAYER 2", True, color)
        WINDOW.blit(screen_text, (WIDTH / 2 + 100, 150))
    pygame.display.update()
    
def controls_of_player(player, player2):
    global x
    global y
    global x2
    global y2
    keys = pygame.key.get_pressed()
    
    MTS(" ", BLACK)

    if keys[pygame.K_w] and y > 20:
        y -= 10
        
    if keys[pygame.K_s] and  y < HEIGHT - 50:
        y += 10

    if keys[pygame.K_UP] and y2 > 20:
        y2 -= 10
        
    if keys[pygame.K_DOWN] and y2 < HEIGHT - 50:
        y2 += 10
    
    player.x = x
    player.y = y
    player2.x = x2
    player2.y = y2
    
    MTS(" ", BLACK)

def main_loop():
    global SCORE1
    global shoot
    global shoot2
    global bullet_img2
    global start
    global SCORE2
    clock = pygame.time.Clock()
    GameExit = False
    while not GameExit == True:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit = True
                
        if SCORE1 > 10 or SCORE2 > 10:
            DMTS(" ", "ORANGE")
            start = False
                
        mx, my = pygame.mouse.get_pos()
                
        if keys[pygame.K_d] or keys[pygame.K_a]:
            if not bullet.x > WIDTH:
                shoot = True
            else:
                shoot = False
                
        if shoot == True:
            bullet.x += 20
                
        else:
            bullet.x = x
            bullet.y = y
            
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            if not bullet2.x < 0:
                shoot2 = True
            else:
                shoot2 = False
                
        if shoot2 == True:
            bullet2.x -= 20
                
        else:
            bullet2.x = x2
            bullet2.y = y2
                       
        if bullet.colliderect(player2):
            shoot = False
            
        if bullet2.colliderect(player):
            shoot2 = False
            
        if SCORE1 > 10 or SCORE2 > 10:
            DMTS(" ", "ORANGE")
            start = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if crs.colliderect(sg_hitbox):
               start = True
               SCORE1 = 0
               SCORE2 = 0
            
        if start == True:    
            controls_of_player(player, player2)
            MTS(" ", BLACK)
            WIN_OR_LOSE()
            score_system()
            MTS(" ", BLACK)
            MTS(" ", BLACK)  
            draw_on_window()
        else:
            home_screen()
            
        crs.x = mx
        crs.y = my
        
        if SCORE1 > 10 or SCORE2 > 10:
            DMTS(" ", "ORANGE")
            start = False
                            
    pygame.quit()
  
if __name__ == "__main__": 
    main_loop()