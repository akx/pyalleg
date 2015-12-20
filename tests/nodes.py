# Uh... bouncing thing. :)

from pyalleg import *
import math,random,time

init()
initGfx(0,320,200)
screen=getScreen()
page=Bitmap(320,200)
initMouse()
initKeyboard()

class Node:
	def __init__(self,x,y):
		self.neighbors=set()
		self.x,self.y=x,y
		self.dx=-3.0+random.random()*6.0
		self.dy=-3.0+random.random()*6.0
	def c(self):
		if self.x>320: self.x=320
		if self.x<0: self.x=0
		if self.y<0: self.y=0
		if self.y>200: self.y=200
		self.x+=self.dx
		self.y+=self.dy
		self.dx*=brake
		self.dy*=brake

	def neighDist(self):
		dists=[]
		for n in self.neighbors:
			dists.append((n,math.sqrt((self.x-n.x)**2.0+(self.y-n.y)**2.0)))
		return dists

def neigh(a,b):
	a.neighbors.add(b)
	b.neighbors.add(a)


nodes=[]
nNodes=10
nNeighs=7
minDist=50.0
attDist=100.0
attEDist=300.0
brake=0.9

for i in range(nNodes):
	a=i/float(nNodes)*6.282
	node=Node(160+math.cos(a)*100,100+math.sin(a)*80)
	nodes.append(node)

for i,n in enumerate(nodes):
	for b in nodes:
		if n!=b:
			neigh(n,b)



while not keyPressed():
	lt=time.time()
	page.clear()
	setAdd(255)
	for n in nodes:
		n.c()

		#for e in n.neighbors:
		#	page.line(n.x,n.y,e.x,e.y,0x888888)
		#page.circle(n.x,n.y,3,0xFFFFFF)

		nds=n.neighDist()
		for ne,nd in nds:
			ang=math.atan2(ne.y-n.y,ne.x-n.x)
			if nd<minDist:
				pwr=1.0-((minDist-nd)/minDist)**2.0
				ne.dx+=pwr*math.cos(ang)
				ne.dy+=pwr*math.sin(ang)
				page.line(n.x,n.y,ne.x,ne.y,0x880000)
			elif nd>attDist and nd<attEDist:
				pwr=1.0-((nd-attDist)/float(attEDist-attDist))**2.0
				ne.dx-=pwr*math.cos(ang)
				ne.dy-=pwr*math.sin(ang)
				page.line(n.x,n.y,ne.x,ne.y,0x008800)
			else:
				page.line(n.x,n.y,ne.x,ne.y,0x000011)


		ang=math.atan2(n.y-100,n.x-160)
		n.dx+=-0.01*math.cos(ang)
		n.dy+=-0.01*math.sin(ang)
	page.blit(screen)
	while time.time()-lt<1/60.0:
		pass