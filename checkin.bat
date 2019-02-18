@echo off

set SCRIPT_PATH=D:\Project\python\spider_exercise

set /a num=%RANDOM%%%60
at 9:%num% python %SCRIPT_PATH%\auto_checkout.py shizhenhua yish8866983