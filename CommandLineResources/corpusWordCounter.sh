#Description: Full directory word finder. Finds the 
#word passed to it as the first variable in all the 
#files ending with .txt in the same directory as this
#script
#Author: John
#Changed: April 28, 2016

for file in *.txt
do
	echo $file
	tr ' ' '\n' < "$file" | grep "$1" | wc -l
done
