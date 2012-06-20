#Program to split triplet file into a smaller format 

import sys
import fileinput
song_file, users_file, triplet_file = sys.argv[1:4]

counter=1;

songs={};
users={};
for line in fileinput.input([song_file]):
	songs[line.rstrip('\n').split(' ')[0]] = counter;
	counter=counter+1;


counter=1;

for line in fileinput.input([users_file]):
	users[line.rstrip('\n').split(' ')[0]] = counter;
	counter=counter+1;

newfile = open("final_triplet.txt","w");

for line in fileinput.input([triplet_file]):
	temp = line.rstrip('\n').split('\t');
	newfile.write(str(users[temp[0]])+" "+str(songs[temp[1]])+" "+temp[2]+'\n');	

newfile.close();
