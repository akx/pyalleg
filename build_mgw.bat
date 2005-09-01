@echo off
echo ================================================================
echo Building PyAlleg (MingW32)
echo ================================================================
python setup.py mingw_build build_ext --compiler=mingw32
if %ERRORLEVEL%==1 goto cerror


echo.
echo ================================================================
echo Installing PyAlleg
echo ================================================================
python setup.py install --skip-build
if %ERRORLEVEL%==1 goto ierror
goto ok

:cerror
echo ================================================================
echo Failed  * Compile error!
echo ================================================================
goto out

:ierror
echo ================================================================
echo Failed  * Install error!
echo ================================================================
goto out

:ok
echo.
echo ================================================================
echo Success * Completed.
echo ================================================================
:out
echo.