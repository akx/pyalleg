# The Linux part of this script is made by Michael Faerber from Allegro.cc.

from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
import os, string, sys


lib_dirs = []
libraries = []
extra_link_args = []


if sys.platform == 'win32':
        print "* Using Windows library set"
        libraries.append('alleg')
else:
        print "* Using allegro-config to determine libraries"
        # linker arguments
        pipe = os.popen('allegro-config --libs', 'r')
        lines = pipe.readlines()
        del pipe

        for line in lines:
                data = string.split(line[:-1])
                for d in data:
                        if d[:2] == '-L': lib_dirs.append(d[2:])
                        elif d[:2] == '-l': libraries.append(d[2:])
                        else: extra_link_args.append(d)

setup(
   name = "PyAlleg",
   version = '0.1.1',
   description = 'Allegro bindings for Python',
   author = 'AKX',
   package_dir={'pyalleg' : 'src'},
   packages=['pyalleg'],
   ext_modules=[ 
      Extension("_pyalleg", ["src/_pyalleg.pyx"], library_dirs = lib_dirs, libraries = libraries, extra_link_args = extra_link_args)
   ],
   cmdclass = {'build_ext': build_ext}
)