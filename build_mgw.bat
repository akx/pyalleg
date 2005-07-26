@echo off
echo ================================================================
echo Building PyAlleg (MingW32)
echo ================================================================
python setup.py build_ext --compiler=mingw32
if %ERRORLEVEL%==1 goto errorout
echo.
echo ================================================================
echo Installing PyAlleg
echo ================================================================
python setup.py install
goto ok
:errorout
echo ================================================================
echo Failed  * Compile error!
echo ================================================================
goto out
:ok
echo.
echo ================================================================
echo Success * Completed.
echo ================================================================
:out
echo.