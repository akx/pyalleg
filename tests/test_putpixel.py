from pyalleg import *
import time,random

def rnd(m): return random.randint(0,m)

init()
initGfx(0,640,480)
screen=getScreen()
for i in range(640):
	c=Color(rnd(256),rnd(256),rnd(256))
	screen.putPixel(i,i%50,c)
	time.sleep(0.01)
