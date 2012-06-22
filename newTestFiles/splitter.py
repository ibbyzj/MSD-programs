#Program to split triplet file into a smaller format 

import sys
import fileinput
#File names to be added, can be changed
song_file, users_file, triplet_file = sys.argv[1:4]

counter=1;
#Song hashmap
songs={};
#user map
users={};

#Reading the song file and adding the song names to a hashmap
for line in fileinput.input([song_file]):
    #Remove newlines from the string and add the song name to the map with the value as the number
	songs[line.rstrip('\n').split(' ')[0]] = counter;
	counter=counter+1;

#reinitialize counter
counter=1;

#Reading the user file and adding the user names to a hashmap
for line in fileinput.input([users_file]):
	users[line.rstrip('\n').split(' ')[0]] = counter;
	counter=counter+1;

newfile = open("final_triplet.txt","w");
#Reading the triplet file containing each name with songs the person listens to, converting this into an easier readable format
for line in fileinput.input([triplet_file]):
	temp = line.rstrip('\n').split('\t');
	newfile.write(str(users[temp[0]])+" "+str(songs[temp[1]])+" "+temp[2]+'\n');	

newfile.close();
