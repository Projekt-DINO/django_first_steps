# django_first_steps
Python Django REST API First Steps

<h3>Example by Alexnder Teusz</h3>

**General**

To learn how Django works and how to implement the REST API you can create a feature branch of this repository to create you own Django project.

**Django Example Project**

I created the example project called **dino** to play with it. You can create a feature branch to use this for studying Django. 

I created it with the command `django-admin startproject dino`



**Git**

- Download the Repository with `git clone https://github.com/Projekt-DINO/django_first_steps.git`. 
- After downloading it you are on the `master branch`, the branch, which should work all time. 
  - Everytime you finish a feature, it will get merged into the master.
    - IMPORTANT: Another person will merge your feature, to search for mistakes and other things like that
- If you want to create a feature branch, please type in `git checkout -b NameOfNewBranch`. 
  - `checkout` means that you leave the current branch and enter the new one.
  - With `-b` you say that the following String is the name of the branch
- If you changed some code in the feature branch you can save these changes with a messasge to remember what you've done. To save the changes you can first find out what changed with `git status`. This command shows all modified or deleted files in your repository. If there is a file written in red, you have to `add` it to your commit changes. 
- Type `git add .` or `git add path/to/file` to add the modified file.
  - With the dot in `git add .` you add all files and not only one.
- After adding all files you can make a `commit`. A commit is a kind of saving process like in Word or other programs. But here you can see your changes compared to earlier commits. To commit your changes type in the following: 
  - `git commit -m "i changed some code"`
    - The `-m` says that the following string is the commit's message.
  - With `git log` you can see all your commits and there messages.
- Now we added all modified files and created a commit with message. The last step is to upload all this stuff to GitHub. Type in the following: 
  - `git push origin NameOfYourFreatureBranch`
    - `push` is the command to uplaod something
    - `origin …` shows the branch you want to update. 
      - IMPORTANT: Never push something in the `master` as it is the head of all branches. Always push your commits in your feature branch. So first check if you are in the right branach with `git branch`. 
- Now we can see our changes on GitHub! PERFECT!!


**Gitignore**

To upload only the important stuff of your branch, you usually create a file called `.gitignore` which ignores some files of your repository like secret keys, for Mac .DS_Store files or other unimportant or secret information.

It looks like this for the example project: 

```
/**/.DS_Store
/**/.idea
/**/globals
```

You can store your secret keys and other globals in the file `globals/globals.py`

**Globals**

Because there are user specific information which other developers shouldn't read, you create a globals file. 
In this file there are all variables which are different from user to user. In this case the file looks like this: <br>
```
GLOBAL_EMAIL = "mail@someServer.de"
GLOBAL_PASS = "password"
GLOBAL_PORT = 465 
GLOBAL_SECURE = False //true if port is 587
```

These information are used by the contact form to send the email. You may understand why these variables are secret... <br>
Another advantage is that all developers just have to change the globals.py file. So they don't have to spend time on finding all variables in the code.

**Contact Site**

To make our sample app a bit more interesting, I added a Contact Form. <br>
Here is the tutorial [Django Python Contact Form Mail]("https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/")


**Django Tutorial**

There is a very good Django tutorial on YouTube. Here is the link: 

https://www.youtube.com/watch?v=FNQxxpM1yOs&t=2s

