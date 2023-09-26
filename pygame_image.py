import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk2_img = pg.transform.rotozoom(kk_img, 2, 1.0)
    kk4_img = pg.transform.rotozoom(kk_img, 4, 1.0)
    kk6_img = pg.transform.rotozoom(kk_img, 6, 1.0)
    kk8_img = pg.transform.rotozoom(kk_img, 8, 1.0)
    kk10_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    tmr = 0
    x = 0
    
    bird_img =[kk_img, kk2_img, kk4_img, kk6_img, kk8_img, 
               kk10_img, kk8_img, kk6_img, kk4_img, kk2_img] 
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [1600-x, 0])
        screen.blit(bird_img[tmr%10], [300,200])
        pg.display.update()
        x += 1
        tmr += 1
        if x>1600:
            x=0
        clock.tick(100)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()