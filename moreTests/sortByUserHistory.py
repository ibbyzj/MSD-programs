#should create file with users as line number and with the song history as "songTitleA playCountA songTitleB playCountB"
import sys
import fileinput
import heapq
test = open("final_triplet.txt","r")
newfile = open("userHistories.txt","w")
count = 1
currentUser = 1
currentHistory = ''
for line in fileinput.input(['final_triplet.txt']):
	temp = line.rstrip('\n')
	triplet = temp.split()
	if count == 1:
		currentUser = triplet[0]
	if currentUser == triplet[0] :
		currentHistory += str(triplet[1]) + '\t' + str(triplet[2]) + '\t'
	else:
		newfile.write(currentHistory + '\n')
		currentHistory = str(triplet[1]) + '\t' + str(triplet[2]) + '\t'
		currentUser = triplet[0]
	count=count+1
test.close();
newfile.close()
