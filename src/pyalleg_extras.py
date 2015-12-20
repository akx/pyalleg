from _pyalleg import Color,HSVColor,rgbHsv,hsvRgb,getRgb
import time

def getTime():
	return time.clock()

class FPSTimer:
	def __init__(self,fps=50.0):
		self.lastTick=getTime()
		self.n=0
		self.fps=float(fps)
		
	def tick(self):
		ifps=1.0/self.fps
		nt=getTime()
		d=ifps-(nt-self.lastTick)
		delay(d)
		self.lastTick=nt
		


##############################################################################
                              ## XColor ##
                              ############
                              
def _wrap(val,mi,ma):
	while val<mi:
		val=ma+val
	while val>ma:
		val=val-ma
	return val
	
def _clamp(val,mi,ma):
	if val<mi: return mi
	if val>ma: return ma
	return val

class XColor:
	def __init__(self,r=0,g=0,b=0):
		self.r=r
		self.g=g
		self.b=b
		
	def getColor(self):
		return Color(self.r,self.g,self.b)
	
	def copy(self):
		return XColor(self.r,self.g,self.b)
	
	def unpack(self,color):
		self.r,self.g,self.b=getRgb(color)
		return self
		
	def set(self,r,g,b):
		self.r,self.g,self.b=r,g,b
		return self
		
	def setHsv(self,h,s,v):
		self.unpack(HSVColor(h,s,v))
		return self
		
	def getHsv(self):
		return rgbHsv(self.r,self.g,self.b)
	
	def shift(self,pairs,gwrap=0):
		for pair in pairs:
			what=pair[0]
			value=pair[1]
			if len(pair)==3:
				wrap=pair[2]
			else:
				wrap=gwrap
			if what=="hue":
				h,s,v=self.getHsv()
				h=h+value
				if wrap==1:   h=_wrap(h,0,360)
				elif wrap==2: h=_clamp(h,0,360)
				self.setHsv(h,s,v)
			if what=="sat":
				h,s,v=self.getHsv()
				s=s+value
				if wrap==1:   s=_wrap(s,0,1)
				elif wrap==2: s=_clamp(s,0,1)
				self.setHsv(h,s,v)
			if what=="val":
				h,s,v=self.getHsv()
				v=v+value
				if wrap==1:   v=_wrap(v,0,1)
				elif wrap==2: v=_clamp(v,0,1)
				self.setHsv(h,s,v)
			if what=="r":
				self.r=self.r+value
				if wrap==1:   self.r=_wrap(self.r,0,255)
				elif wrap==2: self.r=_clamp(self.r,0,255)
			if what=="g":
				self.g=self.g+value
				if wrap==1:   self.g=_wrap(self.g,0,255)
				elif wrap==2: self.g=_clamp(self.g,0,255)
			if what=="b":
				self.b=self.b+value
				if wrap==1:   self.b=_wrap(self.b,0,255)
				elif wrap==2: self.b=_clamp(self.b,0,255)
		return self
	def shift1(self,what,value,wrap=0):
		return self.shift([(what,value,wrap)],wrap)
		
	def __coerce__(self,other):
		if type(other)==int:
			return self.getColor()
		raise TypeError