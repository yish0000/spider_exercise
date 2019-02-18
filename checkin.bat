@echo off

set /a num=%RANDOM%%%60
schtasks /Create /tn checkin /sc once /st 9:%num% /tr "D:\Project\python\auto_checkout.exe shizhenhua yish8866983"