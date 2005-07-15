from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
import sys
if sys.platform=="win32":
	print "* Using Win32 library set"
	libs=["kernel32","user32","gdi32","comdlg32","ole32","dinput","ddraw","dxguid","winmm","dsound","alleg"]
else:
	print "* Using allegro-config to determine libraries"
	libs=["`allegro-config --libs`"]

setup(
   name = "PyAlleg",
   version = '0.1.1',
   description = 'Allegro bindings for Python',
   author = 'AKX',
   package_dir={'pyalleg' : 'src'},
   packages=['pyalleg'],
   ext_modules=[ 
      Extension("_pyalleg", ["src/_pyalleg.pyx"], libraries = libs)
   ],
   cmdclass = {'build_ext': build_ext}
)
