# Git Walkthrough

This is a script of sorts for running the Version Control with Git portion of a Software Carpentry Workshop for Digital Humanities researchers.  It is based on content from the Software Carpentry git-novice lessons.  It diverges from these lessons by placing an emphasis on using GitHub that is not part of the original lessons, particularly using GitHub and markdown to create a simple project website to share work.

## Why Git/GitHub?

There are two reasons to use Git/GitHub:

1. Version control
2. Sharing

### Why (automated) version control
The importance of version control can begin to be understood with the following comic from Jorge Cham's [“Piled Higher and Deeper”](http://www.phdcomics.com)
![](http://swcarpentry.github.io/git-novice/fig/phd101212s.gif)
Rather than keep multiple slight variations of a document through its entire life cycle version control allows for *one* copy of a document to be kept, the most recent, while all the changes made to get it to its current state are held in the background by a program specially designed to track this information.  This saves the need for bizzare naming conventions and holding multiple copies of the same document.

Version control goes well beyond avoiding bizarre naming conventions though and really comes into its own when there are multiple authors working on a document in parallel.  Rather than just accept what any other contributor has written, version control allows those responsible for the document to choose exactly what gets kept and what gets changed.  It even allows for the roll back of content to previous versions when it is determined that those versions are preferred.  Combined with a central repository like GitHub it also provides a backup for your data and the benefits of enterprise class redundant systems.

### Sharing
While sharing information more easily was part of the original purposes for developing Git the ease with which this can be done via GitHub has made it the case that many users do very little with version control at all and use Git/GitHub solely for it's ability to quickly produce web sites for the sharing of information.  GitHub facilitates the Open science Model by giving researchers a publishing platform that provides access to data, papers, presentations, and the like, all through a fairly easy to use web interface.

## The problem with Git
![https://imgs.xkcd.com/comics/git.png](https://imgs.xkcd.com/comics/git.png)

From [https://xkcd.com/1597/](https://xkcd.com/1597/) by Randal Munroe

## Learning Objectives
We're going to make sharing information via GitHub the primary objective of this portion of the workshop and look at version control only in light of sharing.  By doing this we will be placing the emphasis on using GitHub rather than on using Git.  Make no mistake though Git is central to GitHub and must be understood to make effective use of it.  There will be commandline work in this section but it will be treated as secondary to the use of the Git desktop app.  Emphasis will be placed on generating an understanding of the core concepts that power Git and the terms used to refer to these concepts.

**GitHub now has a really excellent series of guides/tutorials that can be found at [https://guides.github.com/](https://guides.github.com/).**

## "Hello World!" Tutorial
GitHub now offers a short tutorial that will give you the core concepts of the system without having to "know how to code, use the command line, or install Git (the version control software that GitHub is built on)."  We'll work through this tutorial as a class and then build on this by installing Git, using the command line, and expanding on the website capabilities of GitHub.

### Get an account
Before we can use the tutorial you will need to have a GitHub account.  You can get this at [github.com](https://github.com/).  Visit the site, click the "Sign up" button at the top of the page, and follow the process.

Once this is done we will begin following the tutorial that can be found at [https://guides.github.com/activities/hello-world/](https://guides.github.com/activities/hello-world/).

What follows for the rest of this section is mostly extraced verbatim from the tutorial.  Content not from the tutorial is prefaced with "!!!".

### Create a repository
1. In the upper right corner, next to your username, click **+** and then click **New repository**.
2. Name your repository 'hello-world'.
3. Write a short description.
4. !!! Leave the repository as **Public**.  Public repositories are free on GitHub and are open to the world.  Private repositories typically have a monthly fee associated with them (as little as $7 for up to 5 repositories).  Exceptions are made for educational related work such as teaching.  See [https://education.github.com/guide/private_repos](https://education.github.com/guide/private_repos)
5. Select **Initialize this repository with a README**.
6. !!! Ignore the .gitignore and license options. .gitignore would hold a list of files to not track, such as transient/temporary files created by various programs while editing code and the like which are only useful to that program at that moment.
7. Click **Create repository**.
![](https://guides.github.com/activities/hello-world/create-new-repo.png =600x)

### Explaing branching
**Branching** is the way to work on different versions of a repository at one time.

By default your repository has one branch named `master` which is considered to be the definitive branch. We use branches to experiment and make edits before committing them to `master`.

When you create a branch off the `master` branch, you’re making a copy, or snapshot, of `master` as it was at that point in time. If someone else made changes to the `master` branch while you were working on your branch, you could pull in those updates.

This diagram shows:

- The `master` branch
- A new branch called `feature` (because we’re doing ‘feature work’ on this branch)
- The journey that `feature` takes before it’s merged into `master`.
- `feature` merginng back into `master`.

![](https://guides.github.com/activities/hello-world/branching.png =575x)

Have you ever saved different versions of a file? Something like:

- `story.txt`
- `story-joe-edit.txt`
- `story-joe-edit-reviewed.txt`

Branches accomplish similar goals in GitHub repositories.

Here at GitHub, our developers, writers, and designers use branches for keeping bug fixes and feature work separate from our `master` (production) branch. When a change is ready, they merge their branch into `master`.

A straightforward walkthrough of branching as part of the GitHub workshflow can be found at [https://guides.github.com/introduction/flow/](https://guides.github.com/introduction/flow/).  It is recommended that this is reviewed.

### Creating a new branch
1. Go to your new repository `hello-world`.
2. Click the drop down at the top of the file list that says **branch: master**.
3. Type a branch name, `readme-edits`, into the new branch text box.
4. Select the blue **Create branch** box or hit “Enter” on your keyboard.

![](https://guides.github.com/activities/hello-world/readme-edits.gif =400x)

Now you have two branches, `master` and `readme-edits`. They look exactly the same, but not for long! Next we’ll add our changes to the new branch.

### Make and commit changes
Bravo! Now, you’re on the code view for your readme-edits branch, which is a copy of master. Let’s make some edits.

On GitHub, saved changes are called commits. Each commit has an associated commit message, which is a description explaining why a particular change was made. Commit messages capture the history of your changes, so other contributors can understand what you’ve done and why.

Make and commit changes

1. Click the `README.md` file.
2. Click the pencil icon in the upper right corner of the file view to edit.
3. In the editor, write a bit about yourself.
4. Write a commit message that describes your changes (at the bottom of the page).
5. Ignore the option to "Create a new branch and start a pull request".  We'll look at what this means and how to do it later. 
6. Click the **Commit changes** button.

![](https://guides.github.com/activities/hello-world/commit.png =500x)

These changes will be made to just the README file on your `readme-edits` branch, so now this branch contains content that’s different from `master`.

> Note that commits are **manual**.  You must explicitly make them.  Commit and commit regularly.

### Open a pull request
Nice edits! Now that you have changes in a branch off of `master`, you can open a *pull request*.

Pull Requests are the heart of collaboration on GitHub and amount to asking someone to merge your content with theirs. When you open a *pull request*, you’re proposing your changes and requesting that someone review and pull in your contributions into their branch.  Pull requests show the differences, or *diffs*, of the content from both branches. The changes, additions, and subtractions are shown in green and red.

As soon as you make a commit, you can open a pull request and start a discussion, even before the code is finished.

By using GitHub’s @mention system in your pull request message, you can ask for feedback from specific people or teams, whether they’re down the hall or 10 time zones away.

You can even open pull requests in your own repository and merge them yourself. It’s a great way to learn the GitHub Flow before working on larger projects.

Step | Screenshot
-|:-:
Click the **Pull Request** tab, then from the Pull Request page, click the green **New pull request** button. |![](https://guides.github.com/activities/hello-world/pr-tab.gif =400x)
Select the branch you made, `readme-edits`, to compare with `master` (the original).|![](https://guides.github.com/activities/hello-world/pick-branch.png =400x)
Look over your changes in the diffs on the Compare page, make sure they’re what you want to submit.|![](https://guides.github.com/activities/hello-world/diff.png =400x)
When you’re satisfied that these are the changes you want to submit, click the big green **Create Pull Request** button.|![](https://guides.github.com/activities/hello-world/create-pr.png =400x)
Give your pull request a title and write a brief description of your changes.|![](https://guides.github.com/activities/hello-world/pr-form.png =400x)

When you’re done with your message, click **Create pull request**!

### Merge your pull request
In this final step, it’s time to bring your changes together – merging your readme-edits branch into the master branch.

1. Click the green Merge pull request button to merge the changes into master.
2. Click Confirm merge.
3. Go ahead and delete the branch, since its changes have been incorporated, with the Delete branch button in the purple box.

![](https://guides.github.com/activities/hello-world/merge-button.png =500x)

**look into creating a conflict**

### Reverting pull request
Reverting a pull request on GitHub creates a new pull request that contains one revert of the merge commit from the original merged pull request.

> Note: You may need to [use Git to manually revert the individual commits](http://git-scm.com/docs/git-revert.html) if:
> 
- Reverting the pull request causes merge conflicts  
- The original pull request was not originally merged on GitHub (for example, using a fast-forward merge on the command line)

1. Under your repository name, click Pull requests.
2. Click on **Closed** to see a list of past pull requests that have been merged.
3. In the "Pull Requests" list, click the pull request you'd like to revert.  In this case it will be the request that we just accepted.
4. Near the bottom of the pull request, click **Revert**.
5. Merge the resulting pull request.
6. Delete the branch made that created this delete.

## Linking your desktop
GitHub is a nice place to start but it makes a lot of assumptions that may not reflect reality, such as:

1. You always have an Internet connection when you want to work on things.
2. You only have text files.
3. You are happy doing all your edits in the GitHub editor.
4. You are happy with the limited control that GitHub gives you over version control via its interface.

Sooner or later one of these assumptions is likely going to be false and when this happens you should look at having Git run on your desktop.  This can be done either via a desktop application or via the commandline.  Note that the commandline tool is *much* more powerful than the desktop app.  The commandline tool is also potentially *much* more confusing and since the point of this portion of the workshop is to get you comfortable using Git for sharing and non-complex version control we'll look at the desktop application now and may return to the commandline tool at the end.

> **Warning:** The desktop app is only available for Windows and Mac.  Linux users will be stuck with the commandline.

### Getting set up

1. The commandline tool can be downloaded for either Mac or Windows at: [https://desktop.github.com/](https://desktop.github.com/)
2. Installation is straightforward.  You will be asked for your GitHub account name and password and then you will be presented with the core interface.
3. Initially this will be empty (unless you already have Git repositories on your computer) so we will need to add your hello-world project.  Do this by clicking the **+** in the top left corner of the screen, clicking **clone** and then selecting "hello-world". (A clone is an exact copy of a repository that you own.) 
4. It will ask you where to put this directory.  Put it on the destop so that it can be easily found.

Go through the parts of the window with them and show how they could revert to an earlier work by clicking at a point on the tree and choosing the **Revert** option from the gear/settings menu.

### Pushing changes directly to master from the desktop

1. Navigate to the hello-world folder on the Desktop and open `README.md` with a text editing tool.  Let's build on the work from earlier this morning and use `nano` if possible.
2. Add some new text to the file.
3. Change a period earlier in the file to an exclamation point.
4. Return to the desktop app and notice that the top of the screen now says that there is **1 Uncommitted Change**.  Click on this notice to review the change.
5. Clicking on the blue bars on the right will turn the associated change on and off.  If you turn off one part of a change make sure to turn of the accompanying part.
6. Add a summary and description.
7. Click **sync**.
8. View the results on GitHub.

> **Challenge:** Discover what happens when the deletion of a line is uncoupled from its replacement (and vice versa) when making commits and then syncing with the repository.
> **Result:** If you only commit the deletion then the line will be deleted and the replacement will not be added.  If you only commit the addition then the orignial line will be left and the addition appended to it.  Consequently it is best **not** to uncouple changes since the results will typically end in confusion.

### Branching on the desktop

Branching is done on the desktop by selecting the right repository and clicking the branch button.

It is important to watch which branch is active in the tree-view.

When done click the **pull request** button.

Branches can be deleted by having the branch active and then choosing **Delete <name of branch>...** from the **Branch** menu.

https://guides.github.com/introduction/getting-your-project-on-github/
https://help.github.com/desktop/guides/
https://help.github.com/desktop/guides/contributing/reverting-a-commit/

### Adding a project
This is as easy as dragging a folder onto the app and then syncronizing it.

## Markdown
Use an online editor to make the rendering of markdown realtime.

* [https://stackedit.io/](https://stackedit.io/)
* [http://dillinger.io/](http://dillinger.io/)

Core things to show:

* \#s to make headings
* \*s to make italics and bold
* \*s and \1s to make lists
* \`s and """s and indents to make code blocks
* \>s to make quotes
* \[]() to make links
* \!\[]() to add images
* \ to escape special characters

Have them make some changes to their README.md and commit them.

Point them to some online guide, perhaps
[https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/)


## Other benefits 

GitHub provides other benefits over the ones looked at so far in detail. These are beyond the scope of this introduction but you can get a sense for what is possible by looking at the GitHub guides found at: [https://guides.github.com](https://guides.github.com).  The most relevant to the work of participants are highlighted here. 

### Collaborating
Giving people access to controlling repositories.  Doesn't seem to be a GitHub tutorial on this.

### Issues
[https://guides.github.com/features/issues/](https://guides.github.com/features/issues/)
Have participants share their hello-world repositories on the Etherpad and partner with each other to push an issue or two.

### Forking
[https://guides.github.com/activities/forking](https://guides.github.com/activities/forking)
Must be done from either GitHub or from the commandline.

### Web pages
[https://guides.github.com/features/pages](https://guides.github.com/features/pages)
Not sure I really want to go here since it opens up the possibility of having to get into HTML syntax.  Perhaps just stick with the markdown based README.md page for the time being...

Could show off [Jentery's page](http://jentery.github.io/inke2016) which is a nice slide show/presentation just to illustrate what is possible.

### Citations
[https://guides.github.com/activities/citable-code](https://guides.github.com/activities/citable-code)

## Commandline control

### setting up Git

Git is a program just like the programs invoked by `ls`, `mv`, and the other commands we looked at during the Commandline portion of this class.  

Draw from Software Carpentry.  Also help available at https://help.github.com/ , particularly Bootcamp, Setup, and Using Git.

They need to be able to:

1. create a repository and turn on Git
2. Make commits
3. Add files
4. Push to GitHub
5. Pull from GitHub
6. See integration with desktop
7. Turn Git off on a directory
8. Creating a repository
Recording changes to files: add, commit, ...
Viewing changes: status, diff, ...
Ignoring files
Working on the web: clone, pull, push, ...
Resolving conflicts
Open licenses
Where to host work, and why

https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf
