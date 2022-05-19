# pyparabole
Drawing paraboles with python

First, import the module:
```python
import pyparabole
```
Then, execute the following command:
```python
pyparabole.draw(iterations,color,size,verbose,startx,starty,endx,endy,frame,framesize,framecolor,speed,clear)
```
where iterations, size, startx, starty, endx, endy, framesize, speed
are integer,
verbose, frame, clear
are booleran
and color, framecolor
are the colors.
To disable the demo mode in DEMO releases, delete the following lines
from the file:
```python
        p.home()
        p.write('PyParabole by NikitaYarosh')
        p.left(90)
        p.bk(10)
        p.write('DEMO MODE')
```
they are located after the loop in the draw function.
