@echo off

set /a num=%RANDOM%%%60
schtasks /Create /f /tn checkin /sc once /st 19:%num% /tr "D:\Project\python\auto_checkout.exe shizhenhua yish8866983"
pause