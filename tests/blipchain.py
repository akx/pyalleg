"""

  BLIPCHAIN
  
  PyAlleg demo game
  
  Objective: High score.
  How-to:    Click on a blip to cause a massive chain reaction.
  Too slow?: Set the pov variable to zero to disable the persistence-of-vision effect.
  
  This game *can* bring my Athlon XP 3200+ to its knees. And it has an arcane slowing
  system.

"""



try:
	import psyco
	psyco.full()
except:
	pass
from pyalleg import *
import math,random
import time

pov=0.1
sw,sh=640,480
np=400



class Blip:
	def __init__(self):
		self.x=random.randint(10,sw-10)
		self.y=random.randint(10,sh-10)
		self.dir=random.randint(0,6282)/1000.0
		self.mode=0
		self.modemx=random.randint(20,45)

	def update(self,x,y):
		if x>self.x-4 and x<self.x+4 and y>self.y-4 and y<self.y+4:
			self.mode=1

		if self.mode>0:
			self.mode+=1
			if self.mode>self.modemx:
				return 2

		self.x+=math.sin(self.dir)
		self.y+=math.cos(self.dir)
		self.dir+=-0.1+random.random()*0.2

		if self.x<0: self.x=sw-1
		if self.y<0: self.y=sh-1
		if self.x>sw: self.x=1
		if self.y>sh: self.y=1
		return (self.mode>0)

	def draw(self,bmp):
		#bmp.circle(self.x,self.y,2+self.mode/3.0,0xFFCC00)
		bmp.putPixel(self.x,self.y,0xFFCC00)
		if self.mode>0:
			#bmp.hline(self.x-self.mode/2,self.y,self.x+self.mode/2,white)
			#bmp.vline(self.x,self.y-self.mode/2,self.y+self.mode/2,white)
			bmp.circle(self.x,self.y,1+self.mode,white)

class Particle:
	def __init__(self,x=0,y=0,dx=0,dy=0):
		self.x,self.y=x,y
		self.dx,self.dy=dx,dy
		self.time=0
	def alive(self):
		return 1
	def update(self):
		self.x+=self.dx
		self.y+=self.dy
		self.time+=1
	def draw(self,bmp):
		bmp.putpixel(self.x,self.y,255)

class Spark(Particle):
	def __init__(self,x,y,d):
		Particle.__init__(self,x,y)
		sp=float(random.randint(5,10))
		self.dx,self.dy=math.cos(d)*sp,math.sin(d)*sp
		self.dt=random.randint(20,65)

	def update(self):
		self.lx,self.ly=self.x,self.y
		Particle.update(self)
		self.dx*=0.95
		self.dy*=0.95
		self.dy+=0.3

	def draw(self,bmp):
		bmp.fastline(self.lx,self.ly,self.x,self.y,white)


	def alive(self):
		if fps<5: return self.time<self.dt/2
		return self.time<self.dt

class Fader(Particle):
	def __init__(self,x,y):
		Particle.__init__(self,x,y)
		self.t=random.randint(0,64)
		self.dx=(-0.5+random.random())
		self.dy=(-0.5+random.random())

	def update(self):
		Particle.update(self)
		self.t+=random.random()*5.0
		self.sh=255-int(self.t)
		if self.sh<0: self.sh=0

	def draw(self,bmp):
		bmp.putPixel(self.x,self.y,grays[self.sh])
		bmp.putPixel(self.x+1,self.y,grays[self.sh/2])
		bmp.putPixel(self.x-1,self.y,grays[self.sh/2])
		bmp.putPixel(self.x,self.y+1,grays[self.sh/2])
		bmp.putPixel(self.x,self.y-1,grays[self.sh/2])
	def alive(self):
		return self.sh>0

class PSystem:
	def __init__(self):
		self.particles=[]
	def add(self,p):
		self.particles.append(p)
	def update(self):
		a=[]
		for p in self.particles:
			p.update()
			if not p.alive():
				a.append(p)
		map(self.particles.remove,a)
	def draw(self,bmp):
		for p in self.particles:
			p.draw(bmp)




init()
initGfx(0,sw,sh)
initKeyboard()
initMouse()
buffer=Bitmap(sw,sh)
if pov>0:
	povbuffer=Bitmap(sw,sh)
	povbuffer.clear()
buffer.clear()
#buffer=getScreen()
screen=getScreen()
grays=[Color(a,a,a) for a in range(256)]
psys=PSystem()

sqrtTable={}
blips=[]
for i in range(np):
	blips.append(Blip())

end=0
white=Color(255,255,255)
cld=0
sco=0
activ=0
droyed=0
left=0
zt=time.clock()
frames=0
fps=999

while end==0:
	if keyDown(constants.KEY_ESC): end=1
	mb,mx,my=mouseB(),mouseX(),mouseY()

	if mb and cld<15:
		ox,oy=mx,my
		cld+=1
	else:
		ox,oy=-100,-100
	if pov>0:
		buffer.clear()
		setTrans(pov*255)
		transMode()
		povbuffer.drawTransSprite(buffer,0,0)
		solidMode()
	else:
		buffer.clear()
	activ=0
	psys.update()
	psys.draw(buffer)
	deld=[]
	chkd=[]
	for n,b in enumerate(blips):
		r=b.update(ox,oy)
		if r==2:
			deld.append(b)
		elif r>0:
			activ+=1
			if random.random()<0.05+fps/240.0:
				psys.add(Fader(b.x,b.y))
			sco+=0.2*(1+activ/2.0)
			chkd.append(b)

	for b in deld:
		sco+=25
		for f in range(random.randint(10,30)):
			psys.add(Spark(b.x,b.y,random.random()*6.282))
		blips.remove(b)
		droyed+=1

	for b in chkd:
		x,y,d=b.x,b.y,b.mode-5
		for z in blips:
			if z!=b and z.mode==0 and abs(z.x-x)<=d and abs(z.y-y)<=d:
				sco+=100
				z.mode=b.mode/4+1

	for b in blips:
		b.draw(buffer)

	if cld<5:
		buffer.rect(mx-4,my-4,mx+4,my+4,white)
		if mb:
			buffer.rect(ox-6,oy-6,ox+6,oy+6,white)
	if buffer!=screen:
		buffer.blit(screen)
		if pov>0:
			buffer.blit(povbuffer)
	frames+=1
	left=len(blips)
	setWindowTitle("%06d a:%03d d:%03d l:%03d ap:%04d fps:%03d"%(sco,activ,droyed,left,len(psys.particles),fps))
	if time.clock()-zt>1:
		fps=frames
		frames=0
		zt=time.clock()
	if fps>60:
		time.sleep(0.01)