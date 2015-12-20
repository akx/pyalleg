# Vector classes.

import math
class Vec2d:
	def __init__(self,x=0.0,y=0.0):
		self.x=float(x)
		self.y=float(y)
	def __add__(self,other):
		return Vec2d(self.x+other.x,self.y+other.y)
	def __sub__(self,other):
		return Vec2d(self.x-other.x,self.y-other.y)
	def __mul__(self,other):
		if type(other)==type(int()) or type(other)==type(float()):
			return Vec2d(self.x*other,self.y*other)
		else:	#dprod
			return self.x*other.x+self.y*other.y
	def __div__(self,other):
		return Vec2d(self.x/other,self.y/other)
	def __repr__(self):
		return "Vec2d(%s,%s)"%(repr(self.x),repr(self.y))
	def __str__(self):
		return "Vec2d(%f,%f)"%(self.x,self.y)
	def dist(self,other):
		return math.hypot(self.x-other.x,self.y-other.y)
	def length(self):
		return math.hypot(self.x,self.y)
	def norm(self):
		l=self.length()
		if l==0: return Vec2d()
		return Vec2d(self.x/l,self.y/l)
	def tup(self):
		return (self.x,self.y)
	def to3d(self):
		return Vec3d(self.x,self.y,0)
	def copy(self):
		return Vec2d(self.x,self.y)

class Vec3d:
	def __init__(self,x=0.0,y=0.0,z=0.0):
		self.x=float(x)
		self.y=float(y)
		self.z=float(z)
	def __add__(self,other):
		return Vec3d(self.x+other.x,self.y+other.y,self.z+other.z)
	def __sub__(self,other):
		return Vec3d(self.x-other.x,self.y-other.y,self.z-other.z)
	def __mul__(self,other):
		if type(other)==type(int()) or type(other)==type(float()):
			return Vec3d(self.x*other,self.y*other,self.z*other)
		else:	#dot product
			return self.x*other.x+self.y*other.y+self.z*other.z
	def __div__(self,other):
		return Vec3d(self.x/other,self.y/other,self.z/other)
	def __repr__(self):
		return "Vec3d(%s,%s,%s)"%(repr(self.x),repr(self.y),repr(self.z))
	def __str__(self):
		return "Vec3d(%f,%f,%f)"%(self.x,self.y,self.z)
	def dist(self,other):
		return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
	def length(self):
		return math.sqrt(self.x**2+self.y**2+self.z**2)
	def lengthEx(self,func):
		return func(self.x**2+self.y**2+self.z**2)
	def norm(self):
		l=self.length()
		if l==0: return Vec3d()
		return self/l
	def normEx(self,func):
		l=self.lengthEx(func)
		if l==0: return Vec3d()
		return self/l

	def xprod(self,other):
		return Vec3d(	self.y*other.z-other.y*self.z,
				self.z*other.x-other.z*self.x,
				self.x*other.z-other.x*self.y)
	def tup(self):
		return (self.x,self.y,self.z)
	def to2d(self):
		return Vec2d(self.x,self.y)
	def copy(self):
		return Vec3d(self.x,self.y,self.z)
