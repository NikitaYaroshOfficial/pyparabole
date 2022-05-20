p = 'nothing'
def init():
    print('Initializing PyParabole...')
    global p
    from turtle import Turtle
    p = Turtle()
    p.hideturtle()
    p.penup()
    print('Done. Use the draw() command to draw amazing paraboles!')
def draw(iterations,color,size,verbose,startx,starty,endx,endy,frame,framesize,framecolor,speed,clear):
    if p!='nothing':
        if verbose:
            print('Getting to draw a parabole... iterations:',iterations,'; Color:',color,'; Pen Size:',size,'; Start Coordinates:',startx,starty,'; End Coorinates:',endx,endy)
            print('Calculating the field size...')
        fieldxsize = endx-startx
        fieldysize = endy-starty
        p.speed(speed)
        if frame:
            p.color(framecolor)
            p.pensize(framesize)
            p.setpos(startx,starty)
            p.pendown()
            p.setpos(startx,endy)
            p.setpos(endx,endy)
            p.setpos(endx,starty)
            p.setpos(startx,starty)
            p.penup()
        if clear:
            p.screen.clearscreen()
        if fieldxsize<=0 or fieldysize<=0:
            print('E1: Illegal field size: ',fieldxsize,'x',fieldysize)
            raise Exception('E1: Illegal field size')
        stepx = fieldxsize / iterations
        stepy = fieldysize / iterations
        p.color(color)
        p.pensize(size)
        ax = startx
        ay = endy
        bx = startx
        by = starty
        for lop in range(1,iterations):
            ay -= stepy
            bx += stepx
            p.setpos(ax,ay)
            p.pendown()
            p.setpos(bx,by)
            p.penup()
        p.home()
        p.write('PyParabole by NikitaYarosh')
        p.left(90)
        p.bk(10)
        p.write('DEMO MODE')
    else:
        print('E0: Module is not initialized')
        raise Exception('E0: Module is not initialized')
init()
