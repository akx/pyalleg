# Laser demo. The "raytracing" is not perfect in resolution.

from pyalleg import *
import math
import time

def mid(x,y,z):
	return max(x, min(y, z))

init()
initGfx(0,320,240)
initKeyboard()
initMouse()
buffer=Bitmap(320,240)
screen=getScreen()

end=0
white=Color(255,255,255)
green=Color(0,192,0)
red=Color(255,0,0)
vn=50
maxd=800
dres=10

px=160
py=120

while end==0:
	#for k in range(128):
	#	if keyDown(k): print k
	mx,my,mz,mb=mouse()

	if keyDown(59): end=1
	if mb==1:
		px,py=mx,my

	buffer.clear()
	for x in range(7):
		for y in range(7):
			spx=20+x*(40+y%5)
			spy=20+y*(40+(x*2)%5)
			buffer.fillRect(spx,spy,spx+15,spy+15,white)

	ang=math.atan2(float(my-py),float(mx-px))
	dx=math.cos(ang)
	dy=math.sin(ang)
	x=px
	y=py
	contacts=[]
	t=time.clock()
	fds=0.99
	while len(contacts)<800 and time.clock()-t<3.0:
		x+=dx
		y+=dy
		if buffer.getPixel(x,y)==white:
			if buffer.getPixel(x-2,y)!=white or buffer.getPixel(x+2,y)!=white:	# left-right wall
				dx*=-1.0
				x+=dx
				contacts.append((x,y))
			else:
				dy*=-1.0
				x+=dy
				contacts.append((x,y))
		elif x<=0 or x>=320:
			dx*=-1.0
			contacts.append((x,y))
		elif y<=0 or y>=240:
			dy*=-1.0
			contacts.append((x,y))
	lx,ly=px,py
	buffer.fillRect(px-2,py-2,px+2,py+2,red)
	#buffer.line(px,py,px+math.cos(ang)*30.0,my+math.sin(ang)*30.0,white)
	buffer.fillRect(mx-1,my-1,mx+1,my+1,white)

	for x,y in contacts:
		buffer.line(lx,ly,x,y,green)
		lx,ly=x,y
	buffer.blit(screen)
