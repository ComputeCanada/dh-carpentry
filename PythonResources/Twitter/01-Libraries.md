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

[This is a really excellent resource and the first of a series.](http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)
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

##Opening & Reading Files
Reading data from files is essential for most computing tasks.  There are a number of ways to open a file within Python and we'll look at three here, quickly covering the most basic so that you understand the fundamentals and then jumping to a more advanced approach that will be helpful.

1. Open a file, look at it's type, then read it, line by line, then close it.
2. Open a file using a specific library to do so (CSV), then close it.
3. Use `with`.  At this stage actually open the JSON file 

Let us open the file with the sample tweet set:

	open('20160308163459-DH2016.json')

What we have just done is run a *function* in Python, passing it a string to use as input.  The `open` function is used to open connections to files so that we can read and write to them.  The string (of characters) that we passed the open function is the filename.  Since it is just a filename and not a full directory or path the open function will look it the directory that the current file/notebook is being run from.

Running this function will produce output that looks like the following:

	<_io.TextIOWrapper name='20160308163459-DH2016.json' mode='r' encoding='UTF-8'>

What we have done is create a connection to the specified file and what is being reported here are the details of that connection.  We can see that it is using the TextIOWrapper method of the Python io (for "input/output") library, the name of the file, that the mode of the connection is 'r' (for "read only"), and the format the contents of the file are expected to be read in.  

We have not actually read the data in the file, only opened a connection to the file.  To read the file we need to create a container to hold the data and copy content from the file into the container line by line.

Mention three types of open files (r,w,a) and emphasize being explicit.



##NLTK

I now have an iPython/Jupyter notebook that has the rough work in it to load Twitter data from a file and plot the most frequent terms.  It could use some tweaking/clean-up but it will serve as a place holder for the moment.

Mapping locations may be a problem since it seems that most DH related tweets don't have geotagging info in them.  At least not so far...

[Within the NLTK is a large corpora of corpora.  This should be shown and the differences from raw text sources made plain but it should not be the primary focus, that must remain on the twitter feed.]

Sentiment Analysis [http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/](http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)

	$ conda install vincent

##TextBlob
[Saw this at the UCalgary course where it was used to quickly do some sentiment analysis.  This would be really nice to do here combined with a graph/chart. 

See http://textminingonline.com/getting-started-with-textblob (but of course there are other options as well.)]

[https://pythonprogramming.net/twitter-sentiment-analysis-nltk-tutorial/](https://pythonprogramming.net/twitter-sentiment-analysis-nltk-tutorial/)

##Neo4j (or other Network Graphing Tool)
I think there is a neo4j library for this (actually, it seems that there isn't).  Be nice to track the connections within the twitter sphere.

[http://mark-kay.net/2014/08/15/network-graph-of-twitter-followers/](http://mark-kay.net/2014/08/15/network-graph-of-twitter-followers/)

Perhaps use [graph-tool](https://graph-tool.skewed.de/) instead?  Or [NetworkX](http://networkx.github.io/).  NetworkX seems to be the better option for ease of install and nice documentation.

##Mallet
(Is there such a library for this?  Could we show how to call it from the command line within Python?  If the latter is where we go then this might warrant a separate lesson...)

[pymallet](https://pypi.python.org/pypi/pymallet/0.1.1) seems to be an option but there is no documentation for it.

##Advanced
This will be a call-out section that will cover how to set-up the system to:

* pull directly from the Twitter stream
* Use the `vincent` library for javascript/D3 compatibility

##Writing Data
Not sure that there will be data to output here.  If there is then just use `with`.  When we 