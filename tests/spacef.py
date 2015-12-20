# A colorful space-filling line algorithm.

from pyalleg import *
import random

w,h=800,600
init()
initGfx(0,w,h)
screen=getScreen()
page=Bitmap(w,h)
initKeyboard()



class Worker:
	chance=0.1
	def __init__(self):
		self.x=random.randint(0,w)
		self.y=random.randint(0,h)
		self.dx=0
		self.dy=0
		while self.dx==0 and self.dy==0:
			self.dx=random.randint(-1,1)
			self.dy=random.randint(-1,1)
		self.l=255.0
		self.hue=random.randint(0,360)

	def do(self,bmp):
		global w,h
		r,g,b=hsvRgb(self.hue,0.9,self.l/255.0)
		bmp.putPixel(self.x,self.y,Color(r,g,b))
		self.l-=1
		self.x+=self.dx
		self.y+=self.dy
		if bmp.getPixel(self.x,self.y) or self.x>w or self.y>h or self.x<0 or self.y<0 or self.l<0:
			workers.remove(self)
		if random.random()<self.chance and len(workers)<1000:
			wk=Worker()
			wk.x=self.x
			wk.y=self.y
			wk.hue=self.hue+random.randint(-20,20)
			wk.l=min(255,self.l*2)

			workers.append(wk)

workers=[]
workers.append(Worker())
page.clear()

while not keyDown(constants.KEY_ESC):
	if keyDown(constants.KEY_SPACE):
		workers.append(Worker())
	if keyDown(constants.KEY_S):
		b=Bitmap(w,h)
		screen.blit(b,0,0,sw=w,sh=h)
		b.save("foo.bmp")
		
	for wk in workers:
		wk.do(page)
	page.blit(screen)
	if len(workers)==0:
		setWindowTitle("0 - SPACE to exit, S to save")
	else:
		setWindowTitle("%d"%len(workers))

