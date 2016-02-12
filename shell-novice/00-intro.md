---
layout: page
title: The Unix Shell
subtitle: Introducing the Shell
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> *   Explain how the shell relates to the keyboard, the screen, the operating system, and users' programs.
> *   Explain when and why command-line interfaces should be used instead of graphical interfaces.

At a high level, computers do four things:

-   run programs
-   store data
-   communicate with each other
-   interact with us

They can do the last of these in many different ways,
including direct brain-computer links and speech interfaces.
Since these are still in their infancy,
most of us use windows, icons, mice, and pointers.
These technologies didn't become widespread until the 1980s,
but their roots go back to Doug Engelbart's work in the 1960s,
which you can see in what has been called
"[The Mother of All Demos](http://www.youtube.com/watch?v=a11JDLBXtPQ)".

Going back even further,
the only way to interact with early computers was to rewire them.
But in between,
from the 1950s to the 1980s,
most people used line printers.
These devices only allowed input and output of the letters, numbers, and punctuation found on a standard keyboard,
so programming languages and interfaces had to be designed around that constraint.

This kind of interface is called a
**command-line interface**, or CLI,
to distinguish it from a
**graphical user interface**, or GUI,
which most people now use.
The heart of a CLI is a **read-evaluate-print loop**, or REPL:
when the user types a command and then presses the enter (or return) key,
the computer reads it,
executes it,
and prints its output.
The user then types another command,
and so on until the user logs off.

This description makes it sound as though the user sends commands directly to the computer,
and the computer sends output directly to the user.
In fact,
there is usually a program in between called a
**command shell**.
What the user types goes into the shell,
which then figures out what commands to run and orders the computer to execute them. Note, the shell is called *the shell* because it encloses the operating system in order to hide some of its complexity and make it simpler to interact with.

A shell is a program like any other.
What's special about it is that its job is to run other programs
rather than to do calculations itself.
The most popular Unix shell is Bash,
the **B**ourne **A**gain **SH** ell
(so-called because it's derived from a shell written by Stephen Bourne --- this
is what passes for wit among programmers).
Bash is the default shell on most modern implementations of Unix
and in most packages that provide Unix-like tools for Windows.

Using Bash or any other shell
sometimes feels more like programming than like using a mouse.
Commands are terse (often only a couple of characters long),
their names are frequently cryptic,
and their output is lines of text rather than something visual like a graph.
On the other hand,
the shell allows us to combine existing tools in powerful ways with only a few keystrokes
and to set up pipelines to handle large volumes of data automatically thus improving productivity and reproducibility.
In addition, the command line is often the easiest way to interact with remote machines and supercomputers.
Familiarity with the shell is near essential to run a variety of specialised tools and resources including high-performance computing systems. As clusters and cloud computing systems become more popular for scientific data crunching,
being able to interact with them is becoming a necessary skill. We can build on the command-line skills covered here to tackle a wide range of scientific questions and computational challenges.

<!--Using "Landry" because of it's gender neutrality-->
## Landry's Pipeline: Starting Point


<!--Point of the fictitious example is to provide a reasonable frame for the rest of the lesson.  To ensure that students are able to relate to the example it needs to appeal to a range of disciplines.-->

Landry has joined an new research group and needs to build a corpus of text files for future analysis (likely either with [Voyant](http://voyant-tools.org/) or [Mallet]().  These files come from [Project Gutenberg](http://www.gutenberg.org/) and need the extra content at the beginning and the end of the document cut out.  There are 100 books in all and each needs to be:

1. Downloaded.
2. Have the extra content stripped.
3. Have the new copy of the file added to a directory that will represent the corpus that will eventually be processed using other tools.

It takes about 3 minutes to find, download, prepare, and save each file.  The good news is that this will "only" take about 300 minutes (5 hours).

The bad news is that that this must all be done by hand,
meaning that the mouse will need to be clicked thousands of times leaving lots of room for errors.  Not to mention the tedium.  The group is talking about "Big Data" anaylsis by getting access to content from other archives and the volume of "by hand" pre-processing this would involve scares Landry.

The next few lessons will explore what she should do instead.
More specifically,
they explain how Landry can use a command shell
to automate the repetitive steps in this processing pipeline.
As a bonus,
once Landry has put a processing pipeline together,
she will be avialable for use by the research group whenever they need more data.
