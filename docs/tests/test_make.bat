@ECHO OFF

REM Test if SPHINXBUILD is set correctly
set SPHINXBUILD=sphinx-build
call make.bat help
if errorlevel 1 (
    echo Test failed: SPHINXBUILD not set correctly
) else (
    echo Test passed: SPHINXBUILD set correctly
)

REM Test if sphinx-build command is found
set SPHINXBUILD=nonexistent-command
call make.bat help
if errorlevel 1 (
    echo Test passed: sphinx-build command not found as expected
) else (
    echo Test failed: sphinx-build command should not be found
)

REM Test if help command works
set SPHINXBUILD=sphinx-build
call make.bat help
if errorlevel 1 (
    echo Test failed: help command did not execute correctly
) else (
    echo Test passed: help command executed correctly
)