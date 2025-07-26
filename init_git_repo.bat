@echo off
echo Initializing Git repository...
git init
git add .
git commit -m "Initial commit"
set /p repo_url=Enter GitHub repository URL (HTTPS): 
git remote add origin %repo_url%
git branch -M main
git push -u origin main
echo ✅ Repo initialized and pushed to GitHub.
pause
