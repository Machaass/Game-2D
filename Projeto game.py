arquivo = open('Dados aluno.txt', 'r')
unica_string = arquivo.read()
arquivo.close()

import pygame 
pygame.init()

pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)


x = 240
y = 450
v = 10
v1 = -50 
v2 = -20 
v3 = -38 
v4 = -30
v5 = -50
y1 = -50
y2 = -20
y3 = -20
y4 = -25
y5 = -50
fundo = pygame.image.load('assets/pista eu.png')
fundo1 = pygame.image.load('assets/falha na pista.png')
carro = pygame.image.load('assets/picwish.png')
carro2 = pygame.image.load('assets/carro 2.png')
carro3 = pygame.image.load('assets/police.png')
carro4 = pygame.image.load('assets/ambu.png')
carro5 = pygame.image.load('assets/f1.png')
tela = pygame.display.set_mode((640,700))
pygame.display.set_caption('Fast and furious favela!')

tela_aberta = True
while tela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= v 
    if comandos[pygame.K_DOWN]:
        y+= v 
    if comandos[pygame.K_RIGHT]:
        x+= v 
    if comandos[pygame.K_LEFT]:
        x-= v 

    y1 -= v1
    y2 -= v2
    y3 -= v3
    y4 -= v4
    y5 -= v5

    if (y1>750):
        y1=-50
    if(y2>=750):
        y2 = -20
    if(y3>=800):
        y3 = -30
    if(y4>=800):
        y4 = -30
    if(y5>=800):
        y5 = -50

    tela.blit(fundo,(0,0))
    tela.blit(fundo1,(275,y1))
    tela.blit(carro2,(80,y2))
    tela.blit(carro4,(275,y4))
    tela.blit(carro3,(400,y3))
    tela.blit(carro5,(0,y3))
    tela.blit(carro, (x,y))

    pygame.display.update()
pygame.quit()
