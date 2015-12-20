# SpaceWarp - yet another PyAlleg demo game.
# Use the cursor keys to steer and SPACE to go faster.

from pyalleg import *
import random,math,time

def newPoint():
	global tunnel

	if len(tunnel)>0:
		lx,ly,lz=map(float,tunnel[-1])[:3]
		nx=lx-(diffic/-2.0)+random.random()*diffic
		ny=ly-(diffic/-2.0)+random.random()*diffic
		nz=lz+15

	else:
		nx,ny,nz=0,0,100
	tunnel.append([nx,ny,nz,random.random()])

def project(x,y,z,zoom):
	return x/z*zoom+160,y/z*zoom+100


init()
initGfx(0,320,200)
screen=getScreen()
page=Bitmap(320,200)
font=Font()
initKeyboard()

diffic=5
plx,ply=0,0
dx,dy=0,0
sp=0.2
zsp=1.1

rsp=sp
rzsp=zsp
brake=0.998
tunnel=[]
np=20
ao=0.0
fog=50.0
starz=0
radius=15.0
dead=0

sqradius=radius**2

newPoint()
while tunnel[-1][2]<200+fog:
	newPoint()


end=0
brmul=1.0
tbr=0.0
score=0
gates=0
perfect=0
zoom=35.0

while not end:
	lft=time.time()
	zsp=rzsp
	sp=rsp

	if keyPressed():
		if keyDown(constants.KEY_ESC): end=1
		if not dead:
			if keyDown(constants.KEY_SPACE):
				sp*=3
				zsp*=3
				score+=50
			if keyDown(constants.KEY_LEFT): dx-=sp
			if keyDown(constants.KEY_RIGHT): dx+=sp
			if keyDown(constants.KEY_UP): dy-=sp
			if keyDown(constants.KEY_DOWN): dy+=sp
			if keyDown(constants.KEY_A): zoom+=5
			if keyDown(constants.KEY_Z): zoom-=5
			if zoom<2: zoom=2
	dx*=brake
	dy*=brake
	plx+=dx
	ply+=dy
	if dead:
		rzsp=(-0.1+rzsp*8.0)/9.0
		dx*=0.5
		dy*=0.5
		brmul=(0.1+brmul*15.0)/16.0
		tbr+=0.05

	r=0
	for i in range(len(tunnel)):
		tunnel[i][2]-=zsp
		if tunnel[i][2]<0:
			r=1
	if r:
		a=tunnel.pop(0)
		if not dead:
			tbr=1.0

			x0=(plx-a[0])**2.0
			y0=(ply-a[1])**2.0

			dsra=math.sqrt(x0+y0)/float(radius)
			accur=100.0-dsra*100.0

			score+=((1.0-dsra)*(1500+diffic*20))
			gates+=1
			diffic+=0.25
			if dsra<0.05:
				perfect=20
				score+=2000+diffic*50
			if dsra>1:
				dead=1
				deadch=a[:2]
				tbr=0.0
			newPoint()
	page.clear()
	ao+=0.05
	#setAdd(125)

	for n in range(len(tunnel)-1,-1,-1):
		pxyz=tunnel[n]
		px,py,pz,pr=pxyz

		if pz<fog and pz>0:
			c=1.0-(pz/fog)
			r,g,b=hsvRgb(pr*360.0,brmul,c**2*brmul)
			cl=Color(r,g,b)
			sz=(c*3.0)**2.0
			x0,y0=project(px-plx,py-ply,pz,zoom)

			if x0>-30 and y0>-30 and x0<350 and y0<230:
				page.circle(x0,y0,sz,cl)
			for p in range(np):
				a=p/float(np)*6.282+ao
				xo,yo=math.cos(a)*radius-plx,math.sin(a)*radius-ply
				x0,y0=project(px+xo,py+yo,pz,zoom)

				if x0>-30 and y0>-30 and x0<350 and y0<230:
					#solidMode()
					#page.circle(x0,y0,sz,cl)

					page.fillCircle(x0,y0,sz,cl)

	page.circle(160,100,10-tunnel[0][2]/fog*10.0,0xFFFFFF)

	page.line(160,100,160-(plx-tunnel[0][0]),100-(ply-tunnel[0][1]),0xFFFFFF)
	if tbr>0:
		tbr=min(tbr,1)
		if dead:
			text="Score: %d (%d gates, difficulty %d)"%(score,gates,diffic*10)
		else:
			text="%d (Accuracy %.1f%%)"%(score,accur)
			tbr*=0.95
		font.draw(page,160,10,Color(tbr*255,tbr*255,tbr*255),text,1)
	if perfect>0:
		font.draw(page,160,100,0xFFFFFF,"Perfect!",1)
		perfect-=1
	page.blit(screen)
	while time.time()-lft<1/30.0:
		pass


