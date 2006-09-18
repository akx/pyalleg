try:
	import psyco
	psyco.profile()
except:
	pass

import random,math,time
from pyalleg import *
from vector import Vec2d
def lim(a,v,b):
	if v<a:return a
	if v>b:return b
	return v

class Ball:
	def __init__(self):
		self.d=Vec2d()
		self.p=Vec2d(random.randint(20,500),random.randint(20,460))
		self.hit=0
		self.mass=random.randint(4,18)
		self.hue=random.randint(0,360)

		r,g,b=hsvRgb(self.hue,0.7,0.5)
		self.color=Color(r,g,b)


	def draw(self,bmp,ac=0):
		solidMode()
		bmp.fillCircle(self.p.x,self.p.y,10,self.color)
		
		if ac:
			bmp.circle(self.p.x,self.p.y,3,0)
		
	def update(self):
		self.p+=self.d
		self.d*=0.99
		if self.p.x>300 or self.p.x<20:
			self.d.x*=-1.0
			self.p.x=lim(20,self.p.x,620)
		if self.p.y>220 or self.p.y<20:
			self.d.y*=-1.0
			self.p.y=lim(20,self.p.y,460)

def doHit(b1,b2):
	a=b1.d
	b=b2.d
	s1=b1.p
	s2=b2.p
	impact=b-a
	impulse=(s2-s1).norm()
	adb=math.atan2(impulse.y,impulse.x)
	impactspeed=impact*impulse
	q=math.sqrt(abs(impactspeed)*b1.mass*b2.mass)*cmp(impactspeed,0)
	impulse*=q
	b1.d=a+impulse/b1.mass
	b2.d=b-impulse/b2.mass

	# Keep 'erroff.
	s=21
	b2.p=b1.p+Vec2d(s*math.cos(adb),s*math.sin(adb))

def doForce(b1,b2):
	h=abs(b1.hue-b2.hue)/360.0*-0.00001
	vec=Vec2d((b1.p.x-b2.p.x)*h,(b1.p.y-b2.p.y)*h)
	b1.d=b1.d+vec
	#b2.d=b2.d-vec

init()
initGfx(0,640,480)
screen=DoubleBuffer()
font=getFont()
initMouse()
initKeyboard()
balls=[]
nballs=25
for i in range(nballs):
	balls.append(Ball())
lmx=0
lmy=0
mx=0
my=0
frames=fps=0
t=time.time()
while not keyPressed():
	screen.clear()
	lmx,lmy=mx,my
	mx,my,mb=mouseX(),mouseY(),mouseB()
	mdx,mdy=mx-lmx,my-lmy
	balls[0].d+=Vec2d(mdx*0.3,mdy*0.3)
	hits=[]
	for b in balls:
		b.hit=0
	for nb,b in enumerate(balls):
		b.update()
		for d in balls:
			if d!=b:
				ds=b.p.dist(d.p)
				if ds<=20:
					hits.append((b.p.tup(),d.p.tup()))
					b.hit=1
					d.hit=1
					doHit(b,d)
				doForce(b,d)
		if 0:
			hx=320+math.cos(b.hue/57.0)*300
			hy=240+math.sin(b.hue/57.0)*200
			screen.line(hx,hy,b.p.x,b.p.y,b.color)
			h=-0.01
			vec=Vec2d((b.p.x-hx)*h,(b.p.y-hy)*h)
			b.d=b.d+vec
		
		b.draw(screen,nb==0)
	#for a,b in hits:
	#	screen.line(a[0],a[1],b[0],b[1],0xFFFFFF)
	screen.flip()
	#if fps>60:
	#	time.sleep(0.01)
	frames+=1
	if time.time()-t>1:
		fps,frames=frames,0
		t=time.time()
		setWindowTitle("FPS: %d"%fps)

