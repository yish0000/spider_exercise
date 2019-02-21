@echo off

set /a num=%RANDOM%%%60
if %num% lss 10 (set num=0%num%)
schtasks /Create /f /tn checkout /sc once /st 21:%num% /tr "D:\Project\python\auto_checkout.exe shizhenhua yish8866983"
pause