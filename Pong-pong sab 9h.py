# Jogo Ping Pong    :)
import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

tela= pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong pong!")

fundo= pygame.Surface((640,480))
fundo=fundo.convert()
fundo.fill((0,0,0))

bar= pygame.Surface((10,50))
bar1=bar.convert()
bar1.fill((0,0,255))
bar2=bar.convert()
bar2.fill((255,0,0))

circ_sur=pygame.Surface((15,15))
circ= pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
bolinha=circ_sur.convert()

bar1_x, bar2_x = 10, 620
bar1_y, bar2_y = 215, 215

bolinha_x, bolinha_y = 307.5, 232.5
bar1_movim = bar2_movim = 0
veloc_x = veloc_y = veloc_circ = 250
bar1_pontos = bar2_pontos = 0
veloc = 0

clock= pygame.time.Clock()
font = pygame.font.SysFont("Arial",40)

while True:
    ###Comandos
    for evt in pygame.event.get():
        if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
            exit()


    #### Movimentação - Seta para cima e para baixo####

    if evt.type==KEYDOWN:     ###### se pressionar tecla #####
        if evt.key==K_UP:
            bar1_movim= -veloc   ### bar1_movim = bar1_movim - veloc
        elif evt.key==K_DOWN:
            bar1_movim = veloc

    elif evt.type == KEYUP:    ##### se soltar a tecla #####
        if evt.key==K_UP:
            bar1_movim = 0
        elif evt.key==K_DOWN:
            bar1_movim=0


    pontos1 = font.render(str(bar1_pontos), True, (255,255,255))
    pontos2 = font.render(str(bar2_pontos),True, (255,255,255))

    tela.blit(fundo, (0,0))
    pygame.draw.rect(tela,(255,255,255),Rect((5,5),(630,470)),2)  ####640,480
    pygame.draw.aaline(tela,(255,255,255),(330,5),(330,473))

    tela.blit(bar1, (bar1_x,bar1_y))
    tela.blit(bar2, (bar2_x,bar2_y))
    tela.blit(bolinha, (bolinha_x,bolinha_y))
    tela.blit(pontos1, (250,210))
    tela.blit(pontos2, (380,210))

    ###### Movimentar a barra  no eixo y ######

    bar1_y += bar1_movim   #### bar1_y = bar1_y + bar1_movim

    ##### Movimentar a bolinha #####
    tempo = clock.tick(50)      #### velocidade da bolinha #####
    tempo_segs= tempo /1000.0

    bolinha_x += veloc_x * tempo_segs
    bolinha_y += veloc_y * tempo_segs
    veloc= veloc_circ * tempo_segs

    ########  Inteligência Artifical (IA) --- barra vermelha ######
    if bolinha_x >= 305:
        if not bar2_y == bolinha_y +7.5:
            if bar2_y < bolinha_y + 7.5:
                bar2_y +=veloc
            if bar2_y > bolinha_y - 42.5:
                bar2_y -= veloc
        else:
            bar2_y== bolinha_y + 7.5

    ####### Impede da barra de sair da tela - restrito ao layout ######
    if bar1_y >=420:     #### caso a borda esteja muito grossa os valores
        bar1_y =420      #### podem alterar ######
    elif bar1_y <=10:    #### tela 640,480  --- x=640 , y=480
        bar1_y=10
    if bar2_y >=420:
        bar2_y=420
    elif bar2_y <=10:
        bar2_y=10

    ####### Detecta a colisão de forma primitiva ---- PODE SER ALTERADO!!! ####
    if bolinha_x <= bar1_x + 10:   #### barra azul
        if bolinha_y >= bar1_y - 7.5 and bolinha_y <= bar1_y +42.5:
            bolinha_x = 20
            veloc_x = -veloc_x
    if bolinha_x >= bar2_x - 15:   #### barra vermelha
        if bolinha_y >= bar2_y - 7.5 and bolinha_y <=bar2_y +42.5:
            bolinha_x=605
            veloc_x = -veloc_x
    if bolinha_x <5:
        bar2_pontos +=1
        bolinha_x,bolinha_y = 320,232.5
        bar1_y,bar2_y = 215,215
    elif bolinha_x >620:
        bar1_pontos +=1
        bolinha_x,bolinha_y = 320,232.5
        bar1_y,bar2_y = 215,215
    if bolinha_y <=10:
        veloc_y =  -veloc_y
        bolinha_y = 10
    elif bolinha_y >= 457.5:
        veloc_y = -veloc_y
        bolinha_y=457.5

    pygame.display.flip()








