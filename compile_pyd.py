from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
import sys
libs=["kernel32","user32","gdi32","comdlg32","ole32","dinput","ddraw","dxguid","winmm","dsound","alleg"]

cont="y"
if len(sys.argv)==1:
	sys.argv.append("build_ext")
	print "This will build a fresh copy of _pyalleg.pyd"
	cont=raw_input("Continue? (y/n)").strip().lower()
	
if cont=="y":
	setup(	name = "PyAlleg",
  		ext_modules=[Extension("_pyalleg", ["_pyalleg.pyx"], libraries=libs,extra_compile_args=["-Wno-unused"])],
  		cmdclass = {'build_ext': build_ext}
		)