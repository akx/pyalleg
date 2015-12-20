# Have you seen that Windows screensaver?

from pyalleg import *
from random import randint
from math import sqrt,atan,atan2,sin,cos
try:
	import psyco
	psyco.full()
except:
	pass

def getRgb(c):
	return (c&0xFF0000)>>16,(c&0xFF00)>>8,c&0xFF

def applyWarper(target,warper,bx,by,scale=1.0):
	w,h=warper.size()
	tw,th=float(w*scale),float(h*scale)
	temp=Bitmap(tw,th)
	for x in range(tw):
		for y in range(th):
			wx=x/tw*w
			wy=y/th*h
			s=warper.getPixel(wx,wy)
			c1,c2,c3=getRgb(s)

			sx=bx+(c1*scale)%tw
			sy=by+(c2*scale)%th
			temp.putPixel(x,y,target.getPixel(sx,sy))
	temp.blit(target,bx,by)
	temp.destroy()
	del temp

init()
initGfx(0,320,240)
initKeyboard()
bm=Bitmap(320,240)
bm.clear()
setTrans(200)
for z in range(120):
	x=randint(0,320)
	y=randint(0,240)
	r=randint(10,30)
	bm.fillCircle(x,y,r,Color(randint(128,255),randint(128,255),randint(128,255)))
	bm.circle(x,y,r,0)
solidMode()
page=Bitmap(320,240)
screen=getScreen()
initMouse()
ws=96
ws2=ws/2.0
ws3=sqrt(2*(ws2**2.0))
warper=Bitmap(ws,ws)
for x in range(ws):
	for y in range(ws):
		xz=float(x-ws2)
		yz=float(y-ws2)

		dc=sqrt(xz**2.0+yz**2.0)/ws3
		dr=atan2(yz,xz)

		#dc=atan(dc)
		dr=dr+(3.141)*(1.0-dc*1.1)**3.0

		ox=ws2+cos(dr)*dc*ws3
		oy=ws2+sin(dr)*dc*ws3
		ox=min(max(0,ox),255)
		oy=min(max(0,oy),255)
		warper.putPixel(x,y,Color(ox,oy,0))

while not keyPressed():
	bm.blit(page)
	applyWarper(page,warper,mouseX(),mouseY(),1.0+mouseB())
	#warper.blit(page)
	page.blit(screen)
