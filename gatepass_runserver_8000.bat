@echo off
echo Changing directory...
cd /d "D:\OneDrive\Corestance Project\GatePass\gatepass"
echo Activating Conda environment...
call conda activate gate_pass_env
if errorlevel 1 (
    echo Failed to activate Conda environment. Exiting.
    pause
    exit /b
)
echo Starting Django server...
start cmd /k python manage.py runserver 0.0.0.0:8000
if errorlevel 1 (
    echo Failed to start the Django server. Exiting.
    pause
    exit /b
)
echo Opening browser...
start http://localhost:8000/superuser/live_entry
pause
