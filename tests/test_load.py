from pyalleg import *
import time,random,math

def rnd(m): return random.randint(0,m)

init()
initGfx(0,640,480)
initKeyboard()
screen=getScreen()
page=Bitmap(640,480)
bitmap=loadBitmap("smiley.bmp")
font1=loadFont("pixelfont.pcx")
font2=loadFont("comic.pcx")
font=getFont()
t=0
sinex=640

# XColor is a class to encapsulate a color value.
# All methods return self in XColor, thus you can say
# XColor().unpack(someColor).shift1("hue",3).getColor()
# to retrieve someColor as a Allegro-compliant color
# with hue shifted by 3. That is, it's equivalent to
# someColor -> rgb triplet
# h,s,v=rgbHsv(r,g,b)
# h+=3
# r,g,b=hsvRgb(h,s,v)
# Color(r,g,b)

sinecolor=XColor(0,0,0)
sinecolor.setHsv(0,1,1)
shifts=	[
		("hue",1.0,1),
		("sat",-0.005,1)
	]
ft=time.time()
frames=0
fps=0
fpslimit=1
while not keyDown(constants.KEY_ESC):
	if keyDown(constants.KEY_Q): fpslimit=1
	if keyDown(constants.KEY_W): fpslimit=0
	if keyDown(constants.KEY_S): page.save("test_load.bmp")
	page.clear()
	t+=0.1
	solidMode()
	for z in range(10):
		sz=200+math.cos(t)*100
		x=320+math.cos(t*0.5+z)*sz
		y=240+math.sin(t*0.6-z)*sz
		bitmap.rotateSprite(page,x-105,y-105,t*(15-z*6))
	sx=sinex
	sinetext="PyAlleg Sine Scroller! FPS: %d"%fps
	sinecolor.shift(shifts,1)
	color=sinecolor.getColor()
	tx=t%20
	if tx<10:
		sinefont=font1
	else:
		sinefont=font2
	
	for n,c in enumerate(sinetext):
		xc=sx
		yc=160+math.sin(t+n*0.5)*20.0
		sinefont.draw(page,xc-1,yc-1,0,c)
		sinefont.draw(page,xc+1,yc+1,0,c)
		sinefont.draw(page,xc-1,yc+1,0,c)
		sinefont.draw(page,xc+1,yc-1,0,c)
		sinefont.draw(page,xc,yc,color,c)
		sx+=sinefont.length(c)+1
	font.draw(page,0,0,0xFFFFFF,"FPS limit[%d]: q/w | S to save image"%fpslimit)
	screen.acquire()
	page.blit(screen)
	screen.release()
	sinex-=1
	if sinex<-600: sinex=640
	frames+=1
	if fps>30 and fpslimit:
		time.sleep(0.01)
	if time.time()-ft>0.2:
		ft=time.time()
		fps=frames*5
		frames=0
