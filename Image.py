import pygame

pygame.init()

sw,sh=500,500

ds=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Adding image and background image")

bi=pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/Python/L31/background.png").convert(),(sw,sh))

pi=pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/Python/L31/hello penguin.png").convert_alpha(),(200,200))

pr=pi.get_rect(center=(sw//2,sh//2-30))

text=pygame.font.Font(None,36).render('Hi Myesha',True,pygame.Color('blue'))
tr=text.get_rect(center=(sw//2,sh//2+110))

def gl():
    c=pygame.time.Clock()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        ds.blit(bi,(0,0))
        ds.blit(pi,pr)
        ds.blit(text,tr)

        pygame.display.flip()

        c.tick(30)
    pygame.quit()
if __name__=='__main__':
    gl()

