@echo off
echo ========================================
echo   Road Guardian - Android Deployment
echo ========================================
echo.

echo Step 1: Checking Flutter installation...
flutter doctor
echo.

echo Step 2: Checking connected devices...
flutter devices
echo.

echo Step 3: Do you have an Android device connected via USB?
echo    - Enable USB Debugging on your phone
echo    - Connect via USB cable
echo    - Accept USB debugging prompt
echo.
pause

echo.
echo Step 4: Cleaning previous builds...
flutter clean
echo.

echo Step 5: Getting dependencies...
flutter pub get
echo.

echo Step 6: Building and running on Android...
echo.
echo IMPORTANT: Make sure backend server is running!
echo    1. Open another terminal
echo    2. cd backend
echo    3. python app.py
echo.
pause

echo.
echo Launching app on Android device...
flutter run --release
echo.

pause
