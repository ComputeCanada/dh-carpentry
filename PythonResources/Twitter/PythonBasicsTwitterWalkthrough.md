<!--
Break out into four sections, each 1/4 day:
1. Syntax overview. Same style as command line section.  Keep this at the basics, fast, and light. Draw from original Python walkthrough.
2. Basic analysis.  JSON. Composition of tweets.  NLTK. Pre-processor. Matplotlib intro.
3. Advanced work.  Sentiment analysis with textblob.  Installing exterior packages with pip / conda.  Maybe MAYBE working with graphs (Might be a problem loading these).
4. Drinking directly from the stream.  How to get the data from Twitter.
5. Extra / Backup.  If they eat all the above content or it fails then we can move to the Zodiac Tool.
-->

This walkthrough is meant to mirror and replace for Humanities scholars---and hopefully some Social Sciences scholars as well--the Python lessons featured on software-carpentry.org.  It is not that numpy or the related techniques shown in the posted lessons have no place in the Humanities or Social Sciences, to the contrary there is much of value to be learned in that lesson, but rather that the methods underpinning that lesson are mostly foreign to these academic disciplines and so stand in the way of learning programming via Python.  By featuring qualitative textual data from a Twitter feed rather than quantitative numeric data from a biological study it is hoped that neither the contents nor the methods will be quite so foreign to those within the Humanities and Social Sciences.  Perhaps this lesson will be of value to those with more quantitative backgrounds as well.

# 1. Python / Jupyter Basics
<!--
We'll build a word counter focusing on topics in the following order:
1. Functions.  print("hello word!")
2. variables vs. strings
3. Operators.
5. Methods.
6. Lists and containers.
7. Control Structures.

The word counter can / will be used in the second part where we look at twitter data and plot the most frequent words.
-->

In this first section we'll quickly cover some basic syntax, control structures, and objects in Python so that when it comes to looking at the basics of actual analysis we are in a better position to see the big picture.

##Boxes and Markdown

Let's begin by typing a brief description of what we are about to do into a _markdown_ box at the top of a new Python 3 workbook in Jupyter notebooks.  Enter something like the following in a markdown box.

	Learning the basics of Python.  When done I will have created my own word counter.

Note that while markdown is raw text on input an interpreter will convert various character sequences into formatting commands that will change the final output.  Change the original line to say:

	**Learning the basics of Python.**  When done I will have created *my own* word counter. 

It will continue to look just as you typed it until you either `hold shift and press enter` or press the `play button` to process the block.  Do either now and your text will render as:

**Learning the basics of Python.**  When done I will have created *my own* word counter.

Note that you can double click on the block to edit the text and then process the block again.

We won't do any more here but you are encouraged to play and experiment on your own later.

There in no single standard to appeal to for markdown formatting although there is general agreement on some core behaviours.  When working within Jupyter you should refer to the [Markdown section of the Jupyter docs](http://jupyter-notebook.readthedocs.org/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html).  You may also find it useful to refer to the [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/) since that is another popular place where Markdown is used.  If you are looking for a template document this guide was written in markdown and should be available wherever you got the PDF version as a .md file.

Note that there are other types of cells/blocks as well.  Make sure that the right cell type is turned on for the content or you won't get the results you are expecting.

##Functions

Let's start working with Python.  Type the following into a code block.

	print("hello world")
	
Notice that the text is coloured.  This is the Python interpreter running in the background telling you what various components of the statement are.

See what the line does by running the cell.

	hello world!

**Congratulations, you have just written and run your first program!** 

Let's look at what happened here. "print" is what is known as a function, meaning that it is a sort of list of commands or processes that the computer is to perform.  Functions are always invoked by writing out the name of the function followed by a set of parentheses. What is inside the parenthesis are the inputs into the function, what it needs or expects to carry out the instructions inside.  There can be many inputs, just one (as is the case here), or no inputs (such functions are known as "empty functions").  Here our input is the text string *hello word!*.  We know that it is a string of text characters because we have wrapped it in quotations.

> What happens when the quotations are:

> a. removed?

> b. swapped with single quotes?

> c. used inconsistently (e.g. no closing quote, open with a single but closed with a double, etc.)?

> d. doubles are used inside singles (e.g. " 'hello wold!' ") or vice versa?

> e. the quote type used inside is the same as is used outside (e.g. " "hello wold!" ")


[Go over errors and show how to escape characters with `\`. If they have done the commandline part of this already then they should be reminded that they have seen this before in reference to spaces in filenames.]

Note that print() is quite happy to take more than one input:

	print("hello","world","!")

or no input

	print()
	
**IMPORTANT:** A major change from Python 2 to Python 3 is the shift from print just being a statement:

	print "hello world!"

to print being implemented as a function (for consistency):

	print("hello world!")

It is a small change that may not seem to matter but it really does because it renders the vast majority of Python 2 programs incompatible with Python 3.

print() is a built-in function, it comes pre-installed and activated with every version of Python.  There are other functions that are built in but which we must load, others that we will have to install separately and then load, and still others that we'll create ourselves.

For the moment though we'll leave these further details of functions behind and look at another core concept, variables.

##Variables
Variables provide us named containers to hold our objects making it easier to pass the contents around within the program without actually having to provide the original object.  For a parallel in language consider how convenient it is to use the phrase "my parents" to refer to people who are my parents rather than carrying them around with me everywhere and having to point to them each time I refer to them.  Let's not get carried away with the analogy.

In the case our hello world example imagine how annoying and counterproductive it would be if what we were working with was not "hello world!" but the text of Moby Dick!

Let's create at use some variables.  We'll start by typing the following:

	

# 2. Basic Analysis
<!--
Here we'll expand on the concepts laid down in part and incorporate the word counter created.  We'll focus on:

1. Planning a program & understanding the value of comments
2. Opening a file
3. Loading data from a file
4. Importing libraries
5. Working with matplotlib

-->

#3. Advanced Analysis
<!--
This is advanced not because it uses really fancy techniques but because it requires the ability to extend Python with non-standard libraries.

-->

#4. Drinking from the Stream
<!--

1. Create a twitter account.
2. Register a project/app at https://apps.twitter.com/
3. Connect to stream in segments
4. Watch stream in real-time
5. Save data
6. Use this data with previously created tools.

This consol looks useful for learning/experimenting with the API: https://dev.twitter.com/rest/tools/console
-->

[Before we begin participants will need to download a file like `20160308163459-DH2016.json` from the course GitHub repository] 

[This is a really excellent resource to use when preparing this lesson.  It is the first of a series.](http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)

[This is the official NLTK twitter doc.](http://www.nltk.org/howto/twitter.html)

##Planning our Program
For us this means understanding the problem and being very clear what the steps are towards creating a solution.  A step is really any part of the program for which we should carry out independent testing to make sure that it works.  This will make the construction of our programs *iterative*.

Most programs can be usefully divided into three major parts:

1. Reading data.
2. Manipultating data.
3. Writing/Displaying data.

So, what we need to do now is add comments that will act as placeholders/sign-posts/instructions as we build the program.  So, we add the following to the top of the file:

	#Task Description: load a corpus of tweets and print a barplot of the most frequently used terms

	#Open the file
	
	#Load the data from the file into a variable
	
	#Slice up the body text of the tweets
	
	#Count the terms
	
	#Produce the chart

[Here is a nice chart tutorial](https://python4mpia.github.io/plotting/advanced.html)

##Opening & Reading Files
Reading data from files is essential for most computing tasks.  There are a number of ways to open a file within Python and we'll look at three here, quickly covering the most basic so that you understand the fundamentals and then jumping to a more advanced approach that will be helpful.

1. Open a file, look at it's type, then read it, line by line, then close it.
2. Open a file using a specific library to do so (CSV), then close it.
3. Use `with`.  At this stage actually open the JSON file 

Let us open the file with the sample tweet set:

	open('20160308163459-DH2016.json')

What we have just done is run a *function* in Python, passing it a string to use as input.  The `open` function is used to open connections to files so that we can read and write to them.  The string (of characters) that we passed the open function is the filename.  Since it is just a filename and not a full directory or path the open function will look in the directory that the current file/notebook is being run from.

Running this function will produce output that looks like the following:

	<_io.TextIOWrapper name='20160308163459-DH2016.json' mode='r' encoding='UTF-8'>

What we have done is create a connection to the specified file and what is being reported here are the details of that connection.  We can see that it is using the TextIOWrapper method of the Python io (for "input/output") library, the name of the file, that the mode of the connection is 'r' (for "read only"), and the format the contents of the file are expected to be read in.  

We have not actually read the data in the file, only opened a connection to the file.  To read the file we need to create a container to hold the data and copy content from the file into the container line by line.

Mention three types of open files (r,w,a), point out that 'r' is the default but emphasize the importance of getting in the habit of being explicit.



##NLTK

I now have an iPython/Jupyter notebook that has the rough work in it to load Twitter data from a file and plot the most frequent terms.  It could use some tweaking/clean-up but it will serve as a place holder for the moment.

Mapping locations may be a problem since it seems that most DH related tweets don't have geotagging info in them.  At least not so far...

[Within the NLTK is a large corpora of corpora.  This should be shown and the differences from raw text sources made plain but it should not be the primary focus, that must remain on the twitter feed.]

Sentiment Analysis [http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/](http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)


##TextBlob
[Saw this at the UCalgary course where it was used to quickly do some sentiment analysis.  This would be really nice to do here combined with a graph/chart. 

See http://textminingonline.com/getting-started-with-textblob (but of course there are other options as well.)]

[https://pythonprogramming.net/twitter-sentiment-analysis-nltk-tutorial/](https://pythonprogramming.net/twitter-sentiment-analysis-nltk-tutorial/)

##Neo4j (or other Network Graphing Tool)
I think there is a neo4j library for this (actually, it seems that there isn't).  Be nice to track the connections within the twitter sphere.

[http://mark-kay.net/2014/08/15/network-graph-of-twitter-followers/](http://mark-kay.net/2014/08/15/network-graph-of-twitter-followers/)

Perhaps use [graph-tool](https://graph-tool.skewed.de/) instead?  Or [NetworkX](http://networkx.github.io/).  NetworkX seems to be the better option for [ease of install](http://networkx.readthedocs.org/en/networkx-1.11/install.html) and nice documentation (Actually, Graph tool also has very nice documentation	).

Graph-Tool is [easily installed via ports](https://graph-tool.skewed.de/download) but not easy for Windows users to install.

	$ conda install networkx

###But how to do this on Windows???
Seems that [the command prompt is used](http://conda.pydata.org/docs/using/using.html#managing-conda).

##Mallet
(Is there such a library for this?  Could we show how to call it from the command line within Python?  If the latter is where we go then this might warrant a separate lesson...)

[pymallet](https://pypi.python.org/pypi/pymallet/0.1.1) seems to be an option but there is no documentation for it. =(

##Advanced
This will be a call-out section that will cover how to set-up the system to:

* pull directly from the Twitter stream
* Use the `vincent` library for javascript/D3 compatibility

	$ conda install vincent
	
* sometimes `conda` doesn't work as a good install option.  `pip` might be a substitute.  For example:

```
Johns-MacBook-Pro:~ simpson$ conda install textblob
Using Anaconda Cloud api site https://api.anaconda.org
Fetching package metadata: ....
Solving package specifications: .
Error:  Package missing in current osx-64 channels: 
  - textblob

You can search for this package on anaconda.org with

    anaconda search -t conda textblob
Johns-MacBook-Pro:~ simpson$ anaconda search -t conda textblob
Using Anaconda Cloud api site https://api.anaconda.org
Run 'anaconda show <USER/PACKAGE>' to get more details:
Packages:
     Name                      |  Version | Package Types   | Platforms      
     ------------------------- |   ------ | --------------- | ---------------
     MickC/textblob            |    0.9.0 | conda           | linux-64       
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     chdoig/textblob           |    0.9.0 | conda           | linux-64, linux-32, osx-64
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     derickl/textblob          |    0.9.0 | conda           | osx-64         
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     hargup/textblob           |          | conda           | linux-64       
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     hisanor/textblob          |   0.11.1 | conda           | linux-64       
                                          : Simple, Pythonic text processing. Sentiment analysis, part-of-speech tagging, noun phrase parsing, and more.
     jacksongs/textblob        |   0.11.0 | conda           | osx-64         
                                          : Simple, Pythonic text processing. Sentiment analysis, part-of-speech tagging, noun phrase parsing, and more.
     memex/textblob            |   0.10.0 | conda           | linux-64, osx-64
     msarahan/textblob         |   0.10.0 | conda           | osx-64         
     pdbaines/textblob         |    0.8.4 | conda           | linux-64       
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     sloria/textblob           |   0.11.0 | conda           | osx-64         
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     sursma/textblob           |    0.8.4 | conda           | win-64         
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     timka/textblob            |    0.9.0 | conda           | win-64         
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     trifacta/textblob         |    0.9.0 | conda           | linux-64       
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
     zhenghao/textblob         |    0.9.1 | conda           | osx-64         
                                          : Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
Found 14 packages
Johns-MacBook-Pro:~ simpson$ anaconda show hisanor/textblob
Using Anaconda Cloud api site https://api.anaconda.org
Name:    textblob
Summary: Simple, Pythonic text processing. Sentiment analysis, part-of-speech tagging, noun phrase parsing, and more.
Access:  public
Package Types:  conda
Versions:
   + 0.11.1

To install this package with conda run:
     conda install --channel https://conda.anaconda.org/jacksongs textblob

Johns-MacBook-Pro:~ simpson$ conda install --channel https://conda.anaconda.org/jacksongs textblob
Using Anaconda Cloud api site https://api.anaconda.org
Fetching package metadata: ......
Solving package specifications: ....

The following specifications were found to be in conflict:
  - conda -> conda-env
  - conda -> pycosat
  - conda -> python 2.7*
  - conda -> pyyaml
  - conda -> requests
  - conda-env (target=conda-env-2.4.5-py35_0.tar.bz2) -> python 2.7*|3.3*|3.4*|3.5*
  - mkl-service (target=mkl-service-1.1.2-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - nltk (target=nltk-3.1-py35_0.tar.bz2) -> numpy *|1.5*|1.6*|1.7*|1.8*|1.9*
  - nltk (target=nltk-3.1-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - nltk (target=nltk-3.1-py35_0.tar.bz2) -> pyyaml
  - nltk (target=nltk-3.1-py35_0.tar.bz2) -> six
  - nose (target=nose-1.3.7-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - numexpr (target=numexpr-2.4.6-np110py35_1.tar.bz2) -> numpy 1.10*|1.11*|1.6*|1.7*|1.8*|1.9*
  - numexpr (target=numexpr-2.4.6-np110py35_1.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - numpy (target=numpy-1.10.4-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - pip (target=pip-8.1.0-py35_0.tar.bz2) -> python 2.7*
  - pip (target=pip-8.1.0-py35_0.tar.bz2) -> setuptools
  - pycosat (target=pycosat-0.6.1-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - python 3.5*
  - pyyaml (target=pyyaml-3.11-py35_1.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - requests (target=requests-2.9.1-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - scikit-learn (target=scikit-learn-0.17-np110py35_2.tar.bz2) -> numpy 1.10*|1.11*|1.5*|1.6*|1.7*|1.8*|1.9*
  - scikit-learn (target=scikit-learn-0.17-np110py35_2.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - scikit-learn (target=scikit-learn-0.17-np110py35_2.tar.bz2) -> scipy
  - scipy (target=scipy-0.17.0-np110py35_0.tar.bz2) -> numpy 1.10*|1.11*|1.5*|1.6*|1.7*|1.8*|1.9*
  - scipy (target=scipy-0.17.0-np110py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - setuptools (target=setuptools-20.2.2-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - six (target=six-1.10.0-py35_0.tar.bz2) -> python 2.6*|2.7*|3.3*|3.4*|3.5*
  - textblob -> nltk
  - textblob -> python 2.7*
  - wheel (target=wheel-0.29.0-py35_0.tar.bz2) -> python 2.7*|3.3*|3.4*|3.5*
Use "conda info <package>" to see the dependencies for each package.

Johns-MacBook-Pro:~ simpson$ pip install textblob
Collecting textblob
  Downloading textblob-0.11.1-py2.py3-none-any.whl (634kB)
    100% |████████████████████████████████| 634kB 636kB/s 
Requirement already satisfied (use --upgrade to upgrade): nltk>=3.1 in ./anaconda/lib/python3.5/site-packages (from textblob)
Installing collected packages: textblob
Successfully installed textblob-0.11.1

```

##Writing Data
Not sure that there will be data to output here.  If there is then just use `with`.  When we 