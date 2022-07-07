import pygame

from pygame.locals import *

from sys import exit

from random import randint 

pygame.init()

# Largura e altura da tela 
largura = 640
altura = 480

# Coordenadas de acordo com as dimensões da tela 
# Com a nave iniciando nesse local, ela irá aparecer no meio da tela 
x = ( largura / 2 ) - 40
y = 380

# Posições em que as naves invasoras irão aparecer no game
x_invasor1 = randint(0, 560)
y_invasor1 = 1

x_invasor2 = randint(0, 560)
y_invasor2 = 1

# Imagens do game 
fundo = pygame.image.load('img/fundo.png')
nave_u = pygame.image.load('img/nave_usuario.png')
invasor_1 = pygame.image.load('img/invasor-1.png')
invasor_2 = pygame.image.load('img/invasor-2.png')

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space Defender')


## Funções do game 

# Nave atirando


# Loop principal onde roda o game 
while True:
    
    tela.fill((0,0,0))
    tela.blit(fundo, (0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    # Comandos para movimentar a nave pela tela 

    if pygame.key.get_pressed()[K_RIGHT]:
        if x < 560:
            x = x + 10
    
    if pygame.key.get_pressed()[K_LEFT]:
        if x > 0:
            x = x - 10

    if pygame.key.get_pressed()[K_SPACE]:
        print('a')

    
    nave_usuario = tela.blit(nave_u, (x, y))

    limite_nave = pygame.draw.line(tela, (13, 13, 9), (0, 395), (640, 395), 1)
    


    
    # Nesse trecho, quando o invasor ultrapassa o limite da nave ele some
    if y_invasor1 != 335:
        y_invasor1 += 1
        nave_inv1 = tela.blit(invasor_1, (x_invasor1, y_invasor1))

    # Trecho que irá movimentar o tiro da nave 
    
        


    
    pygame.display.update()