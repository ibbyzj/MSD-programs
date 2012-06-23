#Program to split triplet file into a smaller format 
#Sort command to sort the final triplet file ( sorts file on count of songs for each user in descending order )- sort -k 1g,3 -k 3gr input_file > out_file

import sys
import fileinput
#File names to be added, can be changed
song_file, users_file, triplet_file = sys.argv[1:4]

counter=1;

songs={};
users={};
#Reading the song file and adding the song names to a hashmap
for line in fileinput.input([song_file]):
	songs[line.rstrip('\n').split(' ')[0]] = counter;
	counter=counter+1;


counter=1;
#Reading the user file and adding the user names to a hashmap
for line in fileinput.input([users_file]):
	users[line.rstrip('\n').split(' ')[0]] = counter;
	counter=counter+1;

newfile = open("final_triplet.txt","w");
#Reading the triplet file containing each name with songs the person listens to, converting this into an easier readable format
for line in fileinput.input([triplet_file]):
	temp = line.rstrip('\n').split('\t');
	newfile.write(str(users[temp[0]])+'\t'+str(songs[temp[1]])+'\t'+temp[2]+'\n');	

newfile.close();
