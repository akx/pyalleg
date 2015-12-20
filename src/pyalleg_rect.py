import math

def setTopLeft(rect,nv):
	w=rect.width
	h=rect.height
	rect.x1=nv[0]
	rect.y1=nv[1]
	rect.x2=rect.x1+w
	rect.y2=rect.y1+h

def setTopRight(rect,nv):
	w=rect.width
	h=rect.height
	rect.x2=nv[0]
	rect.y1=nv[1]
	rect.x1=rect.x2-w
	rect.y2=rect.y2+h

def setBtmLeft(rect,nv):
	w=rect.width
	h=rect.height
	rect.x1=nv[0]
	rect.y2=nv[1]
	rect.x2=rect.x1+w
	rect.y1=rect.y2-h

def setBtmRight(rect,nv):
	w=rect.width
	h=rect.height
	rect.x2=nv[0]
	rect.y2=nv[1]
	rect.x1=rect.x2-w
	rect.y1=rect.y2-h

def setLeftCenter(rect,nv):
	w=rect.width
	h=rect.height
	rect.x1=nv[0]
	rect.y1=nv[1]-h/2.0
	rect.y2=nv[1]+h/2.0
	rect.x2=rect.x1+w


def setRightCenter(rect,nv):
	w=rect.width
	h=rect.height
	rect.x2=nv[0]
	rect.y1=nv[1]-h/2.0
	rect.y2=nv[1]+h/2.0
	rect.x1=rect.x2-w

def setTopCenter(rect,nv):
	w=rect.width
	h=rect.height
	rect.y1=nv[1]
	rect.x1=nv[0]-w/2.0
	rect.x2=nv[0]+w/2.0
	rect.y2=rect.y1+h

def setBtmCenter(rect,nv):
	w=rect.width
	h=rect.height
	rect.y2=nv[1]
	rect.x1=nv[0]-w/2.0
	rect.x2=nv[0]+w/2.0
	rect.y1=rect.y2-h

def setCenter(rect,nv):
	w=rect.width
	h=rect.height
	rect.x1=nv[0]-w/2.0
	rect.x2=nv[0]+w/2.0
	rect.y1=nv[1]-h/2.0
	rect.y2=nv[1]+h/2.0

def setWidth(rect,nv):
	rect.x2=rect.x1+nv

def setHeight(rect,nv):
	rect.y2=rect.y1+nv

def setx1(rect,nv): setTopLeft(rect,(nv,rect.y1))
def sety1(rect,nv): setTopLeft(rect,(rect.x1,nv))

rectHandlers={
		"topLeft":	(lambda r:(r.x1,r.y1),setTopLeft),
		"topRight":	(lambda r:(r.x2,r.y1),setTopRight),
		"btmLeft":	(lambda r:(r.x1,r.y2),setBtmLeft),
		"btmRight":	(lambda r:(r.x2,r.y2),setBtmRight),
		"leftCenter":	(lambda r:(r.x1,(r.y1+r.y2)/2.0),setLeftCenter),
		"rightCenter":	(lambda r:(r.x2,(r.y1+r.y2)/2.0),setRightCenter),
		"topCenter":	(lambda r:((r.x1+r.x2)/2.0,r.y1),setTopCenter),
		"btmCenter":	(lambda r:((r.x1+r.x2)/2.0,r.y2),setBtmCenter),
		"center":	(lambda r:((r.x1+r.x2)/2.0,(r.y1+r.y2)/2.0),setCenter),
		"width":	(lambda r:abs(r.x2-r.x1),setWidth),
		"height":	(lambda r:abs(r.y2-r.y1),setHeight),
		"area":		(lambda r:r.width*r.height,None),
		"perimeter":	(lambda r:r.width*2.0+r.height*2.0,None),
		"longEdge":	(lambda r:max(r.width,r.height),None),
		"shortEdge":	(lambda r:min(r.width,r.height),None),
		"x":		(lambda r:r.x1,setx1),
		"y":		(lambda r:r.y1,sety1),
		"diameter":	(lambda r:math.sqrt(r.width**2+r.height**2),None)
	}

class Rect:

	def __init__(self,x1=0,y1=0,x2=0,y2=0):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
	def __getattr__(self,name):
		if rectHandlers.has_key(name) and rectHandlers[name][0]!=None:
			return rectHandlers[name][0](self)
		raise AttributeError
	def __setattr__(self,name,value):
		if rectHandlers.has_key(name) and rectHandlers[name][1]!=None:
			rectHandlers[name][1](self,value)
		else:
			self.__dict__[name]=value

	def toTuple(self):
		return (self.x1,self.y1,self.x2,self.y2)

	def combine(self,other):
		other=convertToRect(other)
		self.x1=min(self.x1,other.x1)
		self.y1=min(self.y1,other.y1)
		self.x2=max(self.x2,other.x2)
		self.y2=max(self.y2,other.y2)

	def contains(self,other):
		other=convertToRect(other)
		if self.x1<=other.x1 and self.y1<=other.y1 and self.x2>=other.x2 and self.y2>=other.y2:
			return True
		return False
		
	def pointIn(self,x,y):
		if self.x1<=x and self.y1<=y and self.x2>=y and self.y2>=y:
			return True
		return False


	def __eq__(self,other):
		other=convertToRect(other)
		if self.topLeft==other.topLeft and self.btmRight==other.btmRight:
			return True
		return False

	def __lt__(self,other):
		other=convertToRect(other)
		if self.area<other.area:
			return True
		return False

	def __str__(self):
		return "Rect(%.1f, %.1f, %.1f, %.1f)"%(self.x1,self.y1,self.x2,self.y2)

	def move(self,x,y):
		x1,y1=self.topLeft
		x1+=x
		y1+=y
		self.topLeft=(x1,y1)

	def moveTo(self,x,y):
		self.topLeft=(x,y)

	def scale(self,sx,sy):
		self.width=self.width*sx
		self.height=self.height*sy

	def copy(self):
		return Rect(self.x1,self.y1,self.x2,self.y2)

	def dump(self):
		print "Rect %s"%str(self.toTuple())
		keys=rectHandlers.keys()
		keys.sort()
		for k in keys:
			print "  %-20s %s"%(k,self.__getattr__(k))

def convertToRect(r):
	if type(r)==Rect:
		return r
	if type(r) in [tuple,list]:
		l=len(r)
		if l==4:
			return Rect(*r)
		if l==2:
			return Rect(r[0],r[1],r[0],r[1])
	if hasattr(r,"toTuple"):
		return convertToRect(r.toTuple())
	raise TypeError,"Cannot convert %s %s to Rect"%(type(r),str(r))

