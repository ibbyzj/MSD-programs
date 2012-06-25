#Python file to take input as the triplet file and to store the songs per user followed by tabs

import scipy.io
import scipy.sparse
import fileinput
import sys

triplet_file, user_songs = sys.argv[1:3]

#Python yield used to return list of songs for each user
def song_function(triplet_file):
	old_user = 1;
	listy = [];
	for line in open(triplet_file):
		try:
			user_id = int(line.rstrip('\n').split(' ')[0]);
			song_id = int(line.rstrip('\n').split(' ')[1]);
			count = int(line.rstrip('\n').split(' ')[2]);
		except ValueError:
			continue
		if old_user != user_id:
			print(str(user_id*100/110000)+"%......");
			yield listy;
			listy = [];
			old_user = user_id;
		listy.append((song_id));
	yield listy;



#Initialising user_id to 1;	
userid=1;

#This file stores the data
newfile = open(user_songs,"w");

#Keep looping till the last user is reached
for listy in song_function(triplet_file):
	line = str(userid)+'\t';
	for song in listy:
		if song==listy[-1]:
			line+=str(song);
		else:
			line+=(str(song)+'\t');
	line+='\n';	
	userid+=1;
	newfile.write(line);
	
newfile.close();
print("done");
	
	

