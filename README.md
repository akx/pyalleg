PyAlleg 0.1.3.6-b
=================

What is..?
----------

A wrapper for the Allegro library for Python.

Setup instructions
------------------

### Compiling the extension (source packages)

You need to have

-   A working Allegro 4.2 installation.
-   Pyrex.

Thanks to the efforts of Michael Faerber, PyAlleg is now Distutils
compliant. That means you should be able to install it with


    python setup.py build_ext
    python setup.py install

*build\_mgw.bat* can/should be used to build PyAlleg under
[MingW](http://www.mingw.org).

What do I need to distribute Pyalleg programs?
----------------------------------------------

The Distutils dependency tracker should know what. Additionally your
users need alleg42.dll on Windows, or the appropriate libraries on other
platforms.

Test programs
-------------

There are multiple test programs packaged with PyAlleg. (In order of
writing.)

-   test\_putpixel.py\
     The first ever test program. Plots some pixels on the screen.
-   test\_lineofsight.py\
     Testing the Polygon function.
-   test\_show.py\
     Polygon, rectangles, blenders, sound, classes, text output, mouse.
-   blipchain.py\
     PyAlleg's first Official Demo Gamelet.
-   test\_load.py\
     Loading bitmaps and fonts. Also demonstrates the new XColor class.
-   test\_mandel.py\
     Uses Python's complex number class for the famous Mandelbrot
    fractal.
-   test\_mandel.py\
     Uses Python's complex number class for the famous Mandelbrot
    fractal.
-   SpaceWarp.py\
     PyAlleg's second Official Demo Gamelet.
-   nodes.py\
     Um.. yes.
-   poolball.py\
     Pool ball simulation, following Hugo Elias's tutorial.
-   warper.py\
     Remember that Microsoft screensaver?
-   fillers.py\
     More or less interesting filler algorithms.
-   laser.py\
     Faking a bouncing ray using getpixel.
-   test\_ttf.py\
     Tests TTF loading using FreeType2.
-   spacef.py\
     Generates fancy desktop wallpapers. :)

License
-------

PyAlleg has a zlib/libpng style license.

    PyAlleg is Copyright (c) 2005-2006 AKX 

    This software is provided 'as-is', without any express or implied
    warranty. In no event will the authors be held liable for any
    damages arising from the use of this software.

    Permission is granted to anyone to use this software for any
    purpose, including commercial applications, and to alter it and
    redistribute it freely, subject to the following restrictions:

      1. The origin of this software must not be misrepresented;
         you must not claim that you wrote the original software.
         If you use this software in a product, an acknowledgment
         in the product documentation would be appreciated but
         is not required.
      2. Altered source versions must be plainly marked as such,
         and must not be misrepresented as being the original software.
      3. This notice may not be removed or altered from any source
         distribution.
