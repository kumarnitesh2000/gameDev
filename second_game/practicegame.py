import pygame
import time
pygame.init()

win=(800,600)
now_draw=False
last_pos=(0,0)
screen=pygame.display.set_mode(win)
pygame.display.set_caption("myGame")

'''
def show_pos(event):
    pos_show=font.render(str(event),True,(255,0,0))
    screen.blit(pos_show,(100,100))
'''

def draw(event):


    pygame.draw.circle(screen,(0,0,0),event,10)
    print("Drawn")
def roundline(srf, color, start, end):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), 10)


run=True
while run:

    event=pygame.event.wait()
    if event.type == pygame.QUIT:
        run = False
    if event.type==pygame.MOUSEBUTTONDOWN:
        #draw(event.pos)
        pygame.draw.circle(screen, (255,255,255), event.pos, 10)
        now_draw=True
    if event.type == pygame.MOUSEBUTTONUP:
        now_draw = False
    if event.type == pygame.MOUSEMOTION:
        if now_draw:
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)
            roundline(screen, (255,255,255), event.pos, last_pos)
        last_pos = event.pos

    pygame.display.flip()
