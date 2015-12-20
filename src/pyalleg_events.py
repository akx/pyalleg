import pyalleg,time

try:
	set
except:
	import sets
	set=sets.Set

mx=0
my=0
mz=0
mb=0
keysDown=set()

class Event:
	def __init__(self,type,**kw):
		self.type=type
		for k,v in kw.items():
			setattr(self,k,v)

	def dump(self):
		print "Event (%d %s)"%(self.type,eventNames.get(self.type,"unknown"))
		dr=dir(self)
		dr.sort()
		for d in dr:
			f=getattr(self,d)
			if not callable(f) and d[:2]!="__" and d!="type":
				print "  %-12s %s"%(d,repr(f))


MOUSEMOVE=1
MOUSEWHEEL=2
MOUSEDOWN=3
MOUSEUP=4
KEYDOWN=5
KEYUP=6
MOUSEDBLCLICK=7
MOUSEDRAG=8
KEYPRESS=9

USER=50

eventNames={
           	MOUSEMOVE:	"Mouse move",
		MOUSEWHEEL:	"Mouse wheel",
		MOUSEDOWN:	"Mouse down",
		MOUSEUP:	"Mouse up",
		KEYDOWN:	"Key down",
		KEYUP:		"Key up",
		MOUSEDBLCLICK:	"Mouse doubleclick",
		MOUSEDRAG:	"Mouse drag",
		KEYPRESS:	"Key press"}

userEvents=[]
clickTimes=[0.0]*8
dblClickInt=0.25
lastMouseDown=None
dragDist=10
typematicDelay=1.0
typematicRate=0.2
typematic={}
dragging=0

def putEvent(ev):
	userEvents.append(ev)

def getEvents():
	global mx,my,mz,mb,keysDown,userEvents,lastMouseDown,dragging
	nt=time.time()
	events=[]
	nmx,nmy,nmz,nmb=pyalleg.mouse()
	if nmx!=mx or nmy!=my:
		mx=nmx
		my=nmy
		ev=Event(MOUSEMOVE,x=nmx,y=nmy)
		events.append(ev)
		if lastMouseDown!=None:
			ds=abs(mx-lastMouseDown[0])+abs(my-lastMouseDown[1])
			if ds>dragDist:
				dragging=1
				ev.dragging=1
				ev.relCoords=(mx-lastMouseDown[0],my-lastMouseDown[1])
				ev.dragStart=lastMouseDown
	if nmz!=mz:
		mz=nmz
		events.append(Event(MOUSEWHEEL,z=nmz))
	if nmb!=mb:
		for b in range(5):
			bb=1<<b
			if nmb&bb and not mb&bb:	# pressed
				events.append(Event(MOUSEDOWN,button=b+1,x=nmx,y=nmy))
				lastMouseDown=nmx,nmy
			if not nmb&bb and mb&bb:	# released
				dragging=0
				lastMouseDown=None
				events.append(Event(MOUSEUP,button=b+1,x=nmx,y=nmy))
				pt=nt-clickTimes[b]
				if pt<dblClickInt:
					events.append(Event(MOUSEDBLCLICK,button=b+1))
				clickTimes[b]=nt

		mb=nmb
	if pyalleg.keyPressed():
		for i in range(pyalleg.constants.KEY_MAX):
			if pyalleg.keyDown(i) and i not in keysDown:
				keysDown.add(i)
				events.append(Event(KEYDOWN,key=i))
				events.append(Event(KEYPRESS,key=i,typematic=0))
				typematic[i]=time.time()+typematicDelay

	if len(keysDown)>0:
		t=time.time()
		for i in keysDown.copy():
			if not pyalleg.keyDown(i):
				keysDown.remove(i)
				del typematic[i]
				events.append(Event(KEYUP,key=i))
			else:
				if t>=typematic[i]:
					typematic[i]+=typematicRate
					events.append(Event(KEYPRESS,key=i,typematic=1))

	events.extend(userEvents)
	userEvents=[]
	return events

def getKeys():
	global keysDown
	return list(keysDown)


def dragOffset():
	if lastMouseDown:
		return mx-lastMouseDown[0],my-lastMouseDown[1]
	return 0,0

def dragStart():
	if lastMouseDown:
		return lastMouseDown
	return 0,0

def test():
	import pyalleg_events as pyallegev

	pyalleg.init()
	pyalleg.initGfx(0,320,240)
	screen=pyalleg.getScreen()
	pyalleg.initKeyboard()
	pyalleg.initMouse()

	end=0
	while end==0:
		c=255
		if pyallegev.dragging: c=255<<8
		screen.putPixel(pyalleg.mouseX(),pyalleg.mouseY(),c)
		events=pyallegev.getEvents()
		if len(events)>0:
			print pyallegev.getKeys()
			for event in events:
				event.dump()
				if event.type==pyallegev.KEYDOWN and event.key==pyalleg.constants.KEY_ESC:
					end=1
				print

if __name__=="__main__":
	test()
