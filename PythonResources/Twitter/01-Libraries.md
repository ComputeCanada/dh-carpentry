# Libraries

This lesson is meant to mirror and replace for Humanities scholars---and hopefully some Social Sciences scholars as well--the Python 01-numpy lesson featured on software-carpentry.org.  It is not that numpy or the related techniques shown in that lesson has no place in the Humanities or Social Sciences, to the contrary there is much of value to be learned in that lesson, but rather that the methods underpinning that lesson are mostly foreign to these academic disciplines and so stand in the way of learning Python.  By featuring qualitative textual data from a Twitter feed rather than quantitative numeric data from a biological study it is hoped that neither the contents nor the methods will be quite so foreign to those within the Humanities and Social Sciences.  Perhaps this lesson will be of value to those with more quantitative backgrounds as well.

This lesson also introduces multiple libraries rather than a single one, showing multiple ways of working with text.

Graphs and charts will need to feature as well.  Matplotlib and, possibly, the Google chart API.

##Opening & Reading Files
Do this in three stages:
1. Open a file, look at it's type, then read it, line by line, then close it.
2. Open a file using a specific library to do so (CSV), then close it.
3. Use `with`.  At this stage actually open the JSON file 

Mention three types of open files (r,w,a) and emphasize being explicit.

##NLTK

[I wonder if there is a fast way to load JSON data into the NLTK to make it a corpus.  hopefully there is.  If there isn't then we'll need to do loops or the like first and that will hurt the smoothness.]

[Within the NLTK is a large corpora of corpora.  This should be shown and the differences from raw text sources made plain but it should not be the primary focus, that must remain on the twitter feed.]

bar plot of languages?  Times of day?  Map of locations?

##TextBlob
[Saw this at the UCalgary course where it was used to quickly do some sentiment analysis.  This would be really nice to do here combined with a graph/chart.]

##Neo4j
I think there is a library for this.  Be nice to track the connections within the twitter sphere.


##Mallet
(Is there such a library for this?  Could we show how to call it from the command line within Python?  If the latter is where we go then this might warrant a separate lesson...)

##Writing Data
Not sure that there will be data to output here.  If there is then just use `with`.  When we 