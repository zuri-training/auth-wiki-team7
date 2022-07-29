# auth-wiki-team7
It is a userfriendly webapp that has a library of authentication code examples. Any Developer can register in this platform to view and download different authentication code examples, and also make community interactions.

# Our design
[Figma Design link](https://www.figma.com/file/kDCI1y7yvPq16hHCpObLj5/Team-7_Authwiki?node-id=0%3A1)
## Technologies used and why?
- **Figma:**
 A powerful design tool. Use to design all the necessary pages in our website

- **Django:**
 Django is a high-level Python web framework that takes care of much of the hassle of web development, so one can focus on writing their app without needing to reinvent the wheel. It is reassuringly secure and exceedingly scalable.

- **Html, Css, Javascript:**
 Use for frontend development. For implementing the designs

## Features
* `Sign-up`
        Enables users to register their details and gain access to the platform
* `Login`
       It is a security measure designed to prevent unauthorized access to confidential data
* `Comment`
       Commenting or adding suggestions to a post in the form of text 
* `Reactions`
        A user can react to an authentication code by giving it an thumbs-up or thumbs-down 
* `Edit auth code`
        An Auth-Code is a code created by the webapp to help identify the domain name holder and it be edited using this feature.
* `Search Tab`
        It allows users to search for different authentication files in different languages
* `Download`
        Users can download code samples using the download button

* `Edit user details`
       User's credentials can be updated after signup. For example if the user wants to change their name, they can do so here
* `List all users`
       To view all registered users
 
## Requirements needed to be Registered

* Name
* Email
* Password 

When the credential is successfully verified during login, the request is authenticated

# Setup
**[Details about Setup](/backend/readme.md#setup)**


## Branching
### Frontend
All branch names should be prefix with *fn_* which stands for `auth_wiki` example *`fn_login-page`*
1. Create a new branch to make your changes. Run `git checkout -b fn_<branch-name>` to create your working branch e.g *`git checkout -b fn_login-page`*
2. Make the required changes.
### Backend
All branch names should be prefix with *fn_* which stands for `auth_wiki` example *`bn_login-page`*
1. Create a new branch to make your changes. Run `git checkout -b bn_<branch-name>` to create your working branch e.g *`git checkout -b bn_login-page`*
2. Make the required changes.
## Commits
1. Stage the file. `git add <your-file>` that has changed. e.g `git add frontend/index.html` because I made changes to the *index.html* file in the frontend folder. You can use *vscode* or *github Desktop*.
2. Write an explanatory commit message using `git commit -m "<your-message>"` e.g `git commit -m "link style.css file"`.
## Pushing
1. Push your local changes using `git push -u origin <your_branch_name>` e.g `git push -u origin fn_login-page`
2. Visit the remote url to create a pull request (PR).
3. Check if you have merge conflict. If so, then resolve. Get assistance if possible.


Any contributions you make are **greatly appreciated**.
