# Poolball simulator, based upon code from Hugo Elias's
# good-looking textured light-sourced bouncy fun smart
# and stretchy page (http://freespace.virgin.net/hugo.elias/)

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
		self.p=Vec2d(random.randint(20,140),random.randint(20,100))
		self.hit=0
		self.mass=random.randint(4,18)

		r,g,b=hsvRgb(self.mass*20,0.7,0.5)
		self.color=Color(r,g,b)
		r,g,b=hsvRgb(self.mass*20,0.5,0.9)
		self.color2=Color(r,g,b)
		r,g,b=hsvRgb(self.mass*20,0.8,0.7)
		self.color3=Color(r,g,b)

	def draw(self,bmp,ac=0):
		bmp.fillCircle(self.p.x,self.p.y,20,self.color)
		mul=0.1
		bmp.ellipse(self.p.x,self.p.y,abs(math.sin(self.p.x*mul)*20.0),20,self.color3)
		bmp.ellipse(self.p.x,self.p.y,20,abs(math.sin(self.p.y*mul)*20.0),self.color3)
		setTrans(128)
		bmp.fillCircle(self.p.x-7,self.p.y-7,5,self.color2)
		solidMode()
		if ac:
			bmp.circle(self.p.x,self.p.y,3,0)
		bmp.circle(self.p.x,self.p.y,20,0)
		if self.hit!=0:
			setTrans(64)
			bmp.fillCircle(self.p.x,self.p.y,self.mass,0xFFFFFF)
			solidMode()
	def update(self):
		self.p+=self.d
		self.d*=0.99
		if self.p.x>300 or self.p.x<20:
			self.d.x*=-1.0
			self.p.x=lim(20,self.p.x,300)
		if self.p.y>220 or self.p.y<20:
			self.d.y*=-1.0
			self.p.y=lim(20,self.p.y,220)

def doHit(b1,b2):
	a=b1.d
	b=b2.d
	s1=b1.p
	s2=b2.p
	impact=b-a
	impulse=(s2-s1).norm()
	adb=math.atan2(impulse.y,impulse.x)
	impactspeed=impact*impulse
	#print "impactspeed: ",impactspeed
	q=math.sqrt(abs(impactspeed)*b1.mass*b2.mass)*cmp(impactspeed,0)
	impulse*=q
	b1.d=a+impulse/b1.mass
	b2.d=b-impulse/b2.mass

	# Keep 'erroff.
	s=41
	b2.p=b1.p+Vec2d(s*math.cos(adb),s*math.sin(adb))


init()
initGfx(0,320,240)
pg=Bitmap(320,240)
screen=getScreen()
font=getFont()
initMouse()
initKeyboard()
balls=[]
nballs=15
for i in range(nballs):
	balls.append(Ball())
lmx=0
lmy=0
mx=0
my=0
frames=fps=0
t=time.time()
while not keyPressed():
	pg.fillRect(0,0,320,240,0x004400)
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
				if ds<=40:
					hits.append((b.p.tup(),d.p.tup()))
					b.hit=1
					d.hit=1
					doHit(b,d)
		b.draw(pg,nb==0)
	for a,b in hits:
		pg.line(a[0],a[1],b[0],b[1],0xFFFFFF)
	pg.blit(screen)
	if fps>60:
		time.sleep(0.01)
	frames+=1
	if time.time()-t>1:
		fps,frames=frames,0
		t=time.time()
		setWindowTitle("FPS: %d"%fps)

