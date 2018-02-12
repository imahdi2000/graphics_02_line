from display import *
from draw import *

screen = new_screen()
green = [ 0, 255, 0 ]
blue = [37, 198, 188]
yellow = [239, 228, 9]

#draw_line( x0, y0, x1, y1, screen, green )
def test():
    draw_line(250,0,250,500,screen,yellow)
    draw_line(0,250,500,250,screen,yellow)
    draw_line(0,0,500,500,screen,yellow)
#    draw_line(500,0,0,500,screen,yellow)
    draw_line(0,500,500,0,screen,yellow)
    draw_line(0,0,250,500,screen,blue)
    draw_line(0,0,500,250,screen,blue)
    draw_line(500,500,250,0,screen,blue)
#    draw_line(0,500,250,0,screen,blue)
    draw_line(500,500,250,0,screen,blue)
#    draw_line(500,500,0,250,screen,blue)
    draw_line(500,500,-500,0,screen,blue)
#    draw_line(0,250,500,249,screen,green)
    #draw_line(5 * 100, 500, 500, 0, screen, green)





def go():
    test()

    for i in range(1,26):
        draw_line(50,450 + -i,150,450 + -i,screen,green)
    for i in range(1,100):
        draw_line(88,425 + -i,113,425 + -i,screen,green)
    for i in range(1,26):
        draw_line(50,330 + -i,150,330 + -i,screen,green)

    for i in range(1,26):
        draw_line(200,300 + -i,300,300 + -i,screen,green)
    for i in range(1,55):
        draw_line(200,300 + -i,225,300 + -i,screen,green)
    for i in range(1,26):
        draw_line(200,246 + -i,300,246 + -i,screen,green)
    for i in range(1,55):
        draw_line(275,221 + -i,300,221 + -i,screen,green)
        for i in range(1,26):
            draw_line(200,180 + -i,300,180 + -i,screen,green)

    for i in range(1,150):
        draw_line(340,155 + -i,370,155 + -i,screen,green)
    for i in range(1,26):
        draw_line(340,90 + -i,460,90 + -i,screen,green)
    for i in range(1,150):
        draw_line(440,155 + -i,470,155 + -i,screen,green)


#draw_line(50,450,150,450,screen,green)

go()
display(screen)
save_extension(screen, 'img.png')
