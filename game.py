import pygame
from pygame.locals import *
from sys import exit
from random import randrange 
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'img')

pygame.init()

# Largura e altura da tela 
largura = 640
altura = 480

# Coordenadas da nave 
x_nave = ( largura / 2 ) - 40
y_nave = 380

# Criando a fonte para poder gerar o texto na tela 
fonte = pygame.font.SysFont('arial', 40, True, False)

# Variável de controle de pontuação
pontos = 100


# Imagens do game 
fundo = pygame.image.load('img/fundo.png')
nave_u = pygame.image.load('img/nave_usuario.png')
asteroide = pygame.image.load('img/asteroide.png')

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space Runner')


# Criação do relógio para poder controlar o FPS do game 
relogio = pygame.time.Clock()

# Classes do Jogo


class Asteroides(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroide
        self.rect = self.image.get_rect()
        self.rect.x = randrange(50, 600, 50)
        self.rect.y = 100

    def update(self):
        if self.rect.y > altura:
            self.rect.y = -80
            self.rect.x = randrange(50, 600, 50)
            
        self.rect.y += 10


todas_as_sprites = pygame.sprite.Group()

#for i in range(4):
obstaculo1 = Asteroides()
obstaculo2 = Asteroides()
obstaculo3 = Asteroides()
obstaculo4 = Asteroides()
todas_as_sprites.add(obstaculo1, obstaculo2, obstaculo3, obstaculo4)


# Loop principal onde roda o game 
while True:
    
    relogio.tick(30)

    tela.fill((0,0,0))
    tela.blit(fundo, (0, 0))

    mensagem1 = f'Pontos: {pontos}'
    texto_formatado1 = fonte.render(mensagem1, True, (225, 225, 225))

    mensagem2 = f'FIM DE JOGO'
    texto_formatado2 = fonte.render(mensagem2, True, (225, 225, 225))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    todas_as_sprites.draw(tela)
    

    nave = tela.blit(nave_u, (x_nave, y_nave))
    bloco1 = pygame.draw.rect(tela, (0, 0, 0), (x_nave + 10, y_nave + 10, 50, 1))
    

    if bloco1.colliderect(obstaculo1) or bloco1.colliderect(obstaculo2) or bloco1.colliderect(obstaculo3) or bloco1.colliderect(obstaculo4):
        tela.blit(texto_formatado2, (200, 220))
    else:
        # Comandos para movimentar a nave, caso ela não tenha colidido
        if pygame.key.get_pressed()[K_RIGHT]:
            if x_nave < 560:
                x_nave = x_nave + 10
        
        if pygame.key.get_pressed()[K_LEFT]:
            if x_nave > 0:
                x_nave = x_nave - 10
        
        todas_as_sprites.update()
        pontos = pontos + 1

    tela.blit(texto_formatado1, (390, 30))
    
    pygame.display.flip()
 