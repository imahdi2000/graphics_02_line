from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    #check that x0 is bigger than x1
    if (x0 > x1):
        #draw_line( x1, y1, x0, y0, screen, color)
        test = x0
        x0 = x1
        x1 = test
        test = y0
        y0 = y1
        y1 = test
    #check for a point
    if(x0 == x1 and y0 == y1):
        plot(screen, color, x0, y0)

    #change in x (B), change in y (A)
    A = y1 - y0
    B = (-1.0) * (x1 - x0)

    #set initial point
    x = x0
    y = y0

    #check for slope of 0
    if (B == 0):
        while(y <= y1):
            plot(screen, color, x, y)
            y = y + 1
        print "dividing by zero"
        return


    #make a slope, rise over run, y/x
    m = (y1-y0) / (x1-x0)

    #check for octant 1 & 5 using slope
    if (m >= 0 and m <= 1):
        d = (2 * A) + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d = d + (2 * B)
            x = x + 1
            d = d + (2 * A)

    #check for octant 2 & 6
    if (m > 1):
        d = A + (2 * B)
        while (y <= y1):
            plot(screen, color, x,y)
            if (d < 0):
                x = x + 1
                d = d + (2 * A)
            y = y + 1
            d = d + (2 * B)

    # check for 4 and 8
    if (m < 0 and m >= -1):
        d = (2 * A) - B
        while (x <= x1):
            plot(screen,color, x,y)
            if (d < 0):
                y = y -1
                d = d - (2 * B)
            x = x + 1
            d = d + (2 * A)

    if (m < -1):
        d = A - (2 * B)
        while (y >= y1):
            plot(screen,color, x,y)
            if (d > 0):
                x = x + 1
                d = d + (2 * A)
            y = y - 1
            d = d - (2 * B)
