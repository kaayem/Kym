@echo off
:start
cls
echo.
echo.
echo Hi Kaayem What are you working on?
echo ================
echo 1. MM query 
echo 2. GSR
echo 3. MM setup checks
echo 4. quit
echo.
 
set /p x=Pick:
IF '%x%' == '1' GOTO NUM_1
IF '%x%' == '2' GOTO NUM_2
IF '%x%' == '3' GOTO NUM_3
IF '%x%' == '4' GOTO NUM_4
GOTO start

:NUM_1
echo Has the Config file been set up (y/n)?
set /p x=Pick:
IF '%x%' == 'y' GOTO LE_A
IF '%x%' == 'n' GOTO LE_B
pause
GOTO start

:LE_A
cd Mongo_Search
python MongoSearch.py
pause
GOTO start

:LE_B
echo well edit it then you idiot
cd Mongo_Search
Config.xlsx
cd ..
pause
GOTO start


:NUM_2
echo This still needs to be developed
pause
GOTO start

:NUM_3
echo This still needs to be developed
pause
GOTO start

:NUM_4
exit
