# Analyzing Twitter Data

This lesson is meant to mirror and replace for Humanities scholars---and hopefully some Social Sciences scholars as well--the Python 01-numpy lesson featured on software-carpentry.org.  It is not that numpy or the related techniques shown in that lesson has no place in the Humanities or Social Sciences, to the contrary there is much of value to be learned in that lesson, but rather that the methods underpinning that lesson are mostly foreign to these academic disciplines and so stand in the way of learning Python.  By featuring qualitative textual data from a Twitter feed rather than quantitative numeric data from a biological study it is hoped that neither the contents nor the methods will be quite so foreign to those within the Humanities and Social Sciences.  Perhaps this lesson will be of value to those with more quantitative backgrounds as well.

> Learning Objectives
> * Understand the value of comments
> * Plan a program
> * Open a file
> * Loop over the contents of a file, line by line
> * Assign values to variables.
> * Explain what a library is, and what libraries are used for.
> * Load a Python library and use the things it contains.
> * Select individual values and subsections from data.
> * Display simple graphs..

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