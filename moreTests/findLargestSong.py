#Should find highest song index number (for instantiating arrays later)
import sys
import fileinput
import heapq
test = open("final_triplet.txt","r")
newfile = open("highestSongIndexSmall.txt","w")
count = 1
largestIndex = 0
foundOn = 0
for line in fileinput.input(['final_triplet.txt']):
	temp = line.rstrip('\n')
	triplet = temp.split()
	if largestIndex < int(triplet[1]):
		largestIndex = int(triplet[1])
		foundOn=count
	count=count+1
newfile.write( str(largestIndex)+ ' is the largest, found on line '+ str(foundOn))
test.close();
newfile.close()
