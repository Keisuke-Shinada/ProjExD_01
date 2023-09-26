import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk5_img = pg.transform.rotozoom(kk_img, 5, 1.0)
    kk10_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk15_img = pg.transform.rotozoom(kk_img, 15, 1.0)
    tmr = 0
    x = 0
    
    bird_img =[kk_img, kk5_img, kk10_img,kk15_img,kk10_img, kk5_img] 
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(bird_img[tmr%4], [300,200])
        pg.display.update()
        x += 1
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()