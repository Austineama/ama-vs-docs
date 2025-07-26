🚀 GitHub AutoDeploy Toolkit

CONTENTS:
- init_git_repo.bat              : One-click GitHub repo setup and push
- .github/workflows/notebook_auto_convert.yml : GitHub Actions auto convert .ipynb → .py
- streamlit_post_commit.bat      : Auto-launch Streamlit app after commit

HOW TO USE:

1. GIT REPO INITIALIZER:
   Double-click 'init_git_repo.bat', enter your GitHub repo URL when prompted.

2. GITHUB ACTIONS:
   Commit and push your .ipynb files. GitHub will auto-convert them to .py scripts.

3. STREAMLIT AUTO-LAUNCH:
   Place 'streamlit_post_commit.bat' in your .git/hooks folder as 'post-commit'
   Make sure to update 'your_app.py' with the real app filename.

BONUS:
- Make sure 'streamlit' is installed (`pip install streamlit`)
- Create a repo on GitHub before running these tools.
