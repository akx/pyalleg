from pyalleg import *

import time,random,math

class Box:
	def __init__(self):
		self.x=rnd(640)
		self.y=-rnd(300)
		self.dy=random.random()
		self.color=Color(rnd(128),rnd(128),rnd(128))
		
	def do(self,bmp):
		self.y+=self.dy
		if self.y>480: self.dy*=-1.0
		if self.y<0 and self.dy<0:
			random.choice(sounds).play(0,rnd(128),-127+rnd(255))
			self.dy*=-1.0
		bmp.fillRect(self.x-3,self.y-3,self.x+3,self.y+3,self.color)

class Particle:
	def __init__(self):
		self.x=self.y=self.dx=self.dy=0
		
	def update(self,world):		
		self.x+=self.dx
		self.y+=self.dy
		self.dy+=world.gravity
		self.dx+=world.wind
		
	def draw(self,bmp):
		bmp.putPixel(self.x,self.y,Color(255,255,255))

class Flare(Particle):
	def __init__(self):
		Particle.__init__(self)
		self.color=Color(rnd(64),rnd(64),rnd(64))
		self.dx=-2.0+random.random()*4.0
		self.dy=random.random()*-5.0

	def draw(self,bmp):
		setAdd(255)
		for r in range(random.randint(3,5)):
			bmp.fillCircle(self.x,self.y,r,self.color)
			
	def update(self,world):
		Particle.update(self,world)
		if self.y>450 and rnd(10)<2:
			self.dy*=-0.8
		
		
class ParticleWorld:
	def __init__(self):
		self.gravity=0.1
		self.wind=0
		self.particles=[]
		
	def update(self,bmp):
		for n,part in enumerate(self.particles[:]):
			if part.y>bmp.size()[1]+20:
				self.particles.pop(n)
			else:
				part.update(self)
				
	def draw(self,bmp):
		for part in self.particles:
			part.draw(bmp)

def rnd(m): return random.randint(0,m)

init()
initKeyboard()
initMouse()
initGfx(0,640,480)
initSound()

sounds=[]
for i in range(1,5):
	sounds.append(Sample("%d.wav"%i))

particleSound=Sample("part.wav")

screen=getScreen()
font=getFont()
buffer=Bitmap(640,480)
t=time.time()

ty=-50
tx=320
tdx=-3.0+random.random()*6.0
tdy=-3.0

pworld=ParticleWorld()

boxes=[]
for i in range(250+rnd(50)):
	boxes.append(Box())

goodbs=constants.blenders[2:]

lf=0
frames=0
tframes=0
fps=0
fpsTimer=FPSTimer(30)

while not keyPressed():
	e=(time.time()-t)
	
		
	cb=goodbs[int(e/5.0)%len(goodbs)]
	ca=((e/5.0)%1.0)*255
	ver=[]
	buffer.clear()
	

	
	# Draw background boxes.
	solidMode()
	for box in boxes:
		box.do(buffer)
	
	# Draw polygon.
	for i in range(10):
		x=300+math.cos(i/3.0+e)*100
		y=200+math.sin(i/1.5+e*1.5)*70
		ver.append((x,y))
	
	setBlender(cb,ca)
	transMode()
	buffer.polygon(ver,Color(240,122,122))
	
	# Do particles.
	pworld.update(buffer)
	pworld.draw(buffer)
	if (mouseB() and tframes%5==0) or rnd(100)<5:
		nf=Flare()
		nf.x=mouseX()
		nf.y=mouseY()
		pworld.particles.append(nf)
		particleSound.play()

	# Update bouncing text.
	tx+=tdx*0.5
	ty+=tdy*0.5
	tdy+=0.05
	if tx>640 or tx<0:
		tx=tx+tdx*-2.0
		tdx*=-1.0
	if ty>480:
		ty=479
		tdy*=-1.0
		
	solidMode()
	font.draw(buffer,tx,ty,Color(255,255,255),"I love PyAlleg!",1)
	font.draw(buffer,0,0,Color(255,255,255),"FPS: %-3d   Current blender: %s @ %-3d"%(fps,cb,ca))
	buffer.blit(screen)
	#fpsTimer.tick()
	frames+=1
	tframes+=1
	if (e-lf)>1.0:
		lf=e
		fps=frames
		frames=0	

print "Average FPS: %.2f"%(tframes/e)