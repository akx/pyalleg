@echo off
touch _pyalleg.pyx
python compile_pyd.py build_ext --compiler=mingw32
goto v%ERRORLEVEL%
:v0
echo Compilation successful.
copy build\lib.win32-2.4\_pyalleg.pyd _pyalleg.pyd
goto x
:v1
echo **** Failed! ****
:x
echo.