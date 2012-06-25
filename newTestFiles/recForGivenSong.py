#should return the top 10 songs for #25150, based on the most played songs by users with 25150 in their history
import sys
import fileinput
import heapq
test = open("final_triplet.txt","r")
newfile = open("topFor25150.txt","w")
count = 1
count2 = 1
count3 = 1
indexSong = 25150
usersWithSong = [None]
songCounter = [None] * 386213 #highest song index in final_triplet.txt
topSongs = [None] * 10
for line in fileinput.input(['final_triplet.txt']):
	temp = line.rstrip('\n')
	triplet = temp.split()
	if '25150' in triplet[1]:
		usersWithSong.append(triplet[0])
	count=count+1
for line in fileinput.input(['final_triplet.txt']):
	temp = line.rstrip('\n')
	triplet = temp.split()
	if triplet[0] in usersWithSong:
		if songCounter[int(triplet[1])] == None:
			songCounter[int(triplet[1])] = int(triplet[2])
		else:
			songCounter[int(triplet[1])] += int(triplet[2])
	count2=count2+1
topSongCounts = [] 
topSongCounts = heapq.nlargest(10,songCounter)
topSongs = [i for i, j in enumerate(songCounter) if j in topSongCounts]
newfile.write(str(topSongs))
test.close();
newfile.close()
