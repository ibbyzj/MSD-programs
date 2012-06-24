#should create file with song number as line number; each line contains print of dictionary which should read {otherSong:timesPlayed, otherSong2:times2Played ... }
import sys
from pprint import pprint
import fileinput
from collections import defaultdict
test = open("userHistories.txt","r")
newfile = open("songsWithSongs.txt","w")
def key_song(): return defaultdict(other_song)
def other_song(): return dict(play_count=0)
songdict = defaultdict(key_song)
for line in fileinput.input(['userHistories.txt']):
	temp = line.rstrip('\n')
	songCounts = temp.split()
	num = len(songCounts)/2
	for i in range(num):
		outside = 2*i 
		for j in range(num):
			inside = 2*j 
			if outside <> inside:
				songdict[outside][inside] = songCounts[2*j+1]
for i in range(len(songdict)):
	newfile.write(str(songdict[i]) + '\n')
test.close();
newfile.close()
