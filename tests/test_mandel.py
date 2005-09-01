try:
	import psyco
	psyco.full()
except:
	pass
from pyalleg import *
import math,random
import time

init()
initGfx(0,320,200)
screen=getScreen()
initKeyboard()

def brotify(c,il=560):
	#print c
	z=complex(0,0)
	for i in range(il):
		z=z**2+c
		if abs(z)>2.0:
			return i
	return -1

zx=2
for px in range(320):
	for py in range(200):
		x=-zx+float(px)/320.0*(zx*2.0)
		y=-zx+float(py)/200.0*(zx*2.0)
		i=brotify(complex(x,y))
		if i<0:
			pc=0x000000
		else:
			pc=i*332
		screen.putPixel(px,py,pc)
while not keyPressed():
	pass