import pygame

from pygame.locals import *

from sys import exit

pygame.init()

# Largura e altura da tela 
largura = 640
altura = 480

# Coordenadas de acordo com as dimensões da tela 
# Com a nave iniciando nesse local, ela irá aparecer no meio da tela 
x = largura / 2
y = 380

# Imagens do game 
fundo = pygame.image.load('img/fundo.png')
nave_u = pygame.image.load('img/nave_usuario.png')

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space Defender')

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
        if x < 600:
            x = x + 10
    
    if pygame.key.get_pressed()[K_LEFT]:
        if x > 0:
            x = x - 10

    
    nave_usuario = tela.blit(nave_u, (x, y))

    
    pygame.display.update()