# auth-wiki-team7
An authentication library

# Setup
## Setup local environment
1. `git clone https://github.com/zuri-training/auth-wiki-team7.git` to your local. *Don't fork* 
2. `cd auth-wiki-team7`
3. Run `git fetch origin` to fetch for remote updates
4. Pull latest changes from the *main* branch. `git pull origin main`.
## Branching
All branch names should be prefix with *aw_* which stands for `auth_wiki` example *`aw_login-page`*
1. Create a new branch to make your changes. Run `git checkout -b aw_<branch-name>` to create your working branch e.g *`git checkout -b aw_login-page`*
2. Make the required changes.
## Commits
1. Stage the file. `git add <your-file>` that has changed. e.g `git add frontend/index.html` because I made changes to the *index.html* file in the frontend folder. You can use *vscode* or *github Desktop*.
2. Write an explanatory commit message using `git commit -m "<your-message>"` e.g `git commit -m "link style.css file"`.
## Pushing
1. Push your local changes using `git push -u origin <your_branch_name>` e.g `git push -u origin aw_login-page`
2. Visit the remote url to create a pull request (PR).
3. Check if you have merge conflict. If so, then resolve. Get assistance if possible.
