import pygame
import random
from pygame.locals import *
import sys

pygame.init()
fpsClock = pygame.time.Clock()

#width,height = 800,600

width = 1280
height = 600

surface = pygame.display.set_mode((width, height))

altura = 150


rojo_img = pygame.image.load("fondo_rojo.png")
azul_img = pygame.image.load("fondo_azul.png")

fondo_w = 720


linea_img = pygame.image.load("linea_divisoria.png")

piedra_img = pygame.image.load("boton_piedra_normal.png")
papel_img = pygame.image.load("boton_papel_normal.png")
tijera_img = pygame.image.load("boton_tijera_normal.png")

img_width = 162
img_hw = img_width/2

rafa_img = pygame.image.load("rafa.png")

rafa_w = 172
rafa_h = 160

contador_img = pygame.image.load("contador.png")

contador_w = 146

pygame.font.init()
#fuente = pygame.font.SysFont("Comic Sans MS", 48)

fuente = pygame.font.Font("Roboto.ttf", 48)



fg_img = pygame.image.load("fg.png")

#message = fuente.render("Has ganado", True, (0,0,0))


tirada = 0
jugado = False
estado = -1
jugada = ''
ronda = 3

score_jugador = 0
score_ia = 0

while True:       
    surface.blit(rojo_img, (0,0))
    surface.blit(azul_img, (width/2,0))
    
    surface.blit(linea_img, (width/2-2,0))
            
    piedra_rect = surface.blit(piedra_img, (width/4-img_width-img_hw, height/2-img_hw))
    papel_rect = surface.blit(papel_img, (width/4-img_hw, height/2-img_hw))
    tijera_rect = surface.blit(tijera_img, (width/4+img_hw, height/2-img_hw))
    
    
    surface.blit(rafa_img, (width-rafa_w, height-rafa_h))
    
    surface.blit(contador_img, (width/2-contador_w/2, 32))

    contador = fuente.render(str(ronda), True, (0,0,0))
    surface.blit(contador, (width/2-20, 104))
    
    
    if jugado:
        if estado == -1:
            message = fuente.render("", True, (255,255,255))
        elif estado == 0:
            message = fuente.render("Empate", True, (255,255,255))
        elif estado == 1:
            message = fuente.render("Has ganado", True, (255,255,255))
        elif estado == 2:
            message = fuente.render("Has perdido", True, (255,255,255))
        elif estado == 3: #game over
            message = fuente.render("GAME OVER", True, (255,255,255))
            
        surface.blit(fg_img, (0,0))
        surface.blit(message, (width/2, height/2))
        
        
    if estado == 3: #game over
        message = fuente.render("GAME OVER", True, (242,103,62))
        
        if score_jugador == score_ia:
            winner = fuente.render("¡¡¡EMPATE!!!", True, (255,255,255))
        elif score_jugador > score_ia:
           winner = fuente.render("¡¡¡Has Ganado!!!", True, (0,255,0))
        else:
            winner = fuente.render("¡¡¡Has Perdido!!!", True, (203,40,33))

        surface.blit(fg_img, (0,0))
        surface.blit(message, (width/2, height/2))
        surface.blit(winner, (width/2, height/2+92))
        

    if tirada == 1:
        ia_rect = surface.blit(piedra_img, (x,y))
    elif tirada == 2:
        ia_rect = surface.blit(papel_img, (x,y))
    elif tirada == 3:
        ia_rect = surface.blit(tijera_img, (x,y))
        
    if jugada == 'piedra':
        piedra_rect = surface.blit(piedra_img, (width/4-img_width-img_hw, height/2-img_hw))
    elif jugada == 'papel':
        papel_rect = surface.blit(papel_img, (width/4-img_hw, height/2-img_hw))
    elif jugada == 'tijera':
        tijera_rect = surface.blit(tijera_img, (width/4+img_hw, height/2-img_hw))
    
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_pos,y_pos = event.pos
            jugado = False
            jugada = ''
            tirada = 0
            
            if estado == 3:
                ronda = 4
                score_jugador = 0
                score_ia = 0
            
            if estado != -1:
                print("Estado es diferente de -1")
                estado = -1
                ronda = ronda - 1
                
                if ronda == 0:
                    estado = 3
            elif piedra_rect.collidepoint(x_pos,y_pos):
                print("piedra!")
                jugada = "piedra"
                jugado = True
            elif papel_rect.collidepoint(x_pos,y_pos):
                print("Papel!")
                jugada = "papel"
                jugado = True
            elif tijera_rect.collidepoint(x_pos,y_pos):
                print("Tijera!")
                jugada = "tijera"
                jugado = True
            else:
                print("Nada")

            if jugado:
                tirada = random.randint(1,3)
                
                x,y = width*3/4-img_hw, height/2-img_hw

                print(tirada)
                if tirada == 1: #piedra
                    if jugada == "piedra":
                        print("Empate")
                        estado = 0
                    elif jugada == "papel":
                        print("Has ganado")
                        score_jugador = score_jugador + 1
                        estado = 1
                    else:
                        print("Has perdido")
                        score_ia = score_ia + 1
                        estado = 2
                elif tirada == 2: #papel
                    if jugada == "papel":
                        print("Empate")
                        estado = 0
                    elif jugada == "tijera":
                        print("Has ganado")
                        score_jugador = score_jugador + 1
                        estado = 1
                    else:
                        print("Has perdido")
                        score_ia = score_ia + 1
                        estado = 2
                elif tirada == 3: #tijera
                    if jugada == "tijera":
                        print("Empate")
                        estado = 0
                    elif jugada == "piedra":
                        print("Has ganado")
                        score_jugador = score_jugador + 1
                        estado = 1
                    else:
                        print("Has perdido")
                        score_ia = score_ia + 1
                        estado = 2
                        
                    
                
    
    #pygame.draw.circle(surface, (255,0,0), (150, altura), 40, 7)
    
    #altura = altura + 1
    altura += 1
    
    pygame.display.update()
    fpsClock.tick(30)