from pyalleg import *
import math

def mid(x,y,z):
	return max(x, min(y, z))

init()
initGfx(0,640,400)
initKeyboard()
initMouse()
buffer=Bitmap(640,400)
screen=getScreen()

end=0
white=Color(255,255,255)
green=Color(0,192,0)
red=Color(255,0,0)
vn=360
maxd=800
dres=2
while end==0:
	for k in range(128):
		if keyDown(k): print k
	mx,my,mz,mb=mouse()
	
	if mb==1 or keyDown(59): end=1

	buffer.clear()
	for x in range(10):
		for y in range(10):
			spx=20+x*40
			spy=20+y*40
			if x%5!=1:
				buffer.fillRect(spx,spy,spx+15,spy+15,white)
	vr=[]
	for p in range(vn):
		ang=p/float(vn)*6.282
		for d in range(0,maxd,dres):
			x=mx+math.cos(ang)*d
			y=my+math.sin(ang)*d
			#x=mid(0,x,640)
			#y=mid(0,y,480)
			if buffer.getPixel(x,y)==white:
				break
			buffer.putPixel(x,y,red)
		vr.append((x,y))	
	transMode()
	setTrans(96)
	buffer.polygon(vr,green)
	solidMode()
	buffer.putPixel(mx,my,red)
	buffer.blit(screen)