# Removes the preamble and postscript from any specified Project Gutenberg
# file in a directory.

for file in *.txt
do
	# Find the start and end lines of the file with line numbers
	# Using grep with the -n flag to get the lines with the line number out front
	# Pipe this to the cut tool which will divide the line at the colon and take 
	# the first field
	startNum=$(grep -n "START OF THIS PROJECT GUTENBERG" $file | cut -f1 -d:)
	endNum=$(grep -n "END OF THIS PROJECT GUTENBERG" $file | cut -f1 -d:)
	# echo $startNum
	# echo $endNum

	if [ -n "$startNum" ]
	then
		if [ -n "$endNum" ]
		then
			# Do the endNum minus startNum math
			(( headCutNum = $endNum - $startNum ))

			# Remove the .txt from the filename
			# trick from http://www.thegeekstuff.com/2010/07/bash-string-manipulation/
			outFile=${file%.*}
			# echo $outFile
	
			# Output the clean version using head to cut the tail and
			# tail to cut the head.
			head -$endNum $file | tail -$headCutNum > "$outFile"-clean2.txt

			
		fi
	fi
done

