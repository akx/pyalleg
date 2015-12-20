# Different fill algorithms.

from pyalleg import *
import random,math,types

class Badfill:
	nodeOrder=[(-1,0),(0,-1),(1,0),(0,1)]
	def __init__(self,bmp,x,y,tc):
		self.bmp=bmp
		self.gc=bmp.getPixel(x,y)
		self.tc=tc
		self.n=[]
		self.sp=(x,y)
		self._a((x,y))
		self.astep=None
		self.bw,self.bh=bmp.size()[:2]
	def do(self):
		self.step=0
		self.preDo()
		while len(self.n)>0:
			#p=random.randint(0,len(self.n)-1)
			#p=-1

			p=self.selectNode()
			if p<-len(self.n): p=-len(self.n)
			if p>=len(self.n): p=len(self.n)-1
			z=self.n.pop(int(p))
			self.lp=z
			self._do(z)
			if self.astep:
				if self.astep(self):
					return 1
			self.step+=1
		return 0
	def _a(self,z):
		if z not in self.n:
			self.bmp.putPixel(z[0],z[1],0x008000)
			self.n.append(z)
	def _ta(self,z):
		if self.bmp.getPixel(z[0],z[1])==self.gc:
			self._a(z)

	def _do(self,z):
		x,y=z
		for z in self.nodeOrder:
			self._ta((x+z[0],y+z[1]))
		self.bmp.putPixel(x,y,self.tc)

	def selectNode(self):
		return 0
	def preDo(self):
		pass

class OrganicBadfill(Badfill):
	def selectNode(self):
		return self.step%(1+len(self.n))
class RandomBadfill(Badfill):
	def selectNode(self):
		return random.randint(0,len(self.n)-1)
class WiggleBadfill(Badfill):
	def selectNode(self):
		return -random.randint(0,4)
class HmmBadfill(Badfill):
	def preDo(self): self.lp=self.sp
	def selectNode(self):
		#n1,n2=self.sp,self.lp
		n1,n2=self.n[0],self.n[-1]
		e=int(math.hypot(n1[0]-n2[0],n1[1]-n2[1]))

		e>>=3
		return -int(e)%len(self.n)
class WaveBadfill(Badfill):
	def selectNode(self):
		n=len(self.n)/2.0
		return n+math.sin(self.step/62.8)*n
class LeftFirstBadfill(Badfill):
	def selectNode(self):
		v=10000
		n=0
		for i,z in enumerate(self.n):
			if z[0]<v: n,v=i,z[0]
		return n

class SortBadfill(Badfill):
	ssb=0

class SumSortBadfill(SortBadfill):
	def selectNode(self):
		self.n.sort(None,sum)
		return self.ssb

class MulSortBadfill(SortBadfill):
	def selectNode(self):
		self.n.sort(None,lambda l:l[0]*l[1])
		return self.ssb

class PosSortBadfill(SortBadfill):
	speed=0
	def getPos(self): pass
	def selectNode(self):
		px,py=self.getPos()
		if self.speed==0:
			self.n.sort(None,lambda l: math.hypot(l[0]-px,l[1]-py))
		else:
			self.n.sort(None,lambda l: (abs(l[0]-px)+abs(l[1]-py)))
		return self.ssb

class CenterSortBadfill(PosSortBadfill):
	def getPos(self):
		return (self.bw/2.0,self.bh/2.0)

class AtanSortBadfill(SortBadfill):
	def selectNode(self):
		x,y=self.bw/2.0,self.bh/2.0
		self.n.sort(None,lambda l:math.atan2(l[0]-x,l[1]-y)*math.hypot(l[0]-x,l[1]-y))
		return self.ssb

def cc(i):
	if keyDown(constants.KEY_SPACE):
		setWindowTitle("N: %05d   Step: %05d"%(len(i.n),i.step))
	if keyDown(constants.KEY_ESC):
		return 1
	return 0

classes=[]
for i in dir():
	p=eval(i)
	if type(p) is types.ClassType:
		if p.__module__=="__main__" and i!="SortBadfill":
			classes.append((i,p))

print "===================="
print "PYALLEG FILLERS DEMO"
print "===================="
print "Select algorithm: "
print "(IMHO the OrganicBadFill algorithm is the most interesting.)"
print
for i,(n,c) in enumerate(classes):
	print "%-2d : %s"%(i,n)
n=int(raw_input(">"))
if n<0: n=0
if n>=len(classes): n=len(classes)-1
print classes[n][0]
init()
w,h=400,300
initGfx(0,w,h)
initKeyboard()
screen=getScreen()
for i in range(9):
	screen.fillCircle(random.randint(0,w),random.randint(0,h),20,0xFFFFFF)



bf=classes[n][1](screen,random.randint(0,w),random.randint(0,h),0xFF0000)

bf.ssb=0
bf.speed=1
bf.astep=cc
bf.do()
print bf.step
