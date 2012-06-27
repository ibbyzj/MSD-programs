#Test final file to write the results for users


import scipy.io
import scipy.sparse
import fileinput
import sys
import numpy

#test_output => Matrix file
#test_triplet => Triplet file
#out_file => output file with 500 song integers per line
test_output, test_triplet, output_file = sys.argv[1:4]

#This is a python function that reads the triplet file, and returns a list of songs per user
def song_function(test_triplet):
	old_user = 1;
	#Lis to hold songs for user_id
	listy = [];
	for line in open(test_triplet):
		try:
			user_id = int(line.rstrip('\n').split(' ')[0]);
			song_id = int(line.rstrip('\n').split(' ')[1]);
			count = int(line.rstrip('\n').split(' ')[2]);
		except ValueError:
			continue
		#If the user_id is different than the previous then empty the list and return it
		if old_user != user_id:
			yield listy;
			listy = [];
			old_user = user_id;
		listy.append((song_id,count));
	yield listy;




#Read the colisten matrix
colisten = scipy.io.mmread(file(test_output)).tocsr();
print("done reading matrix");

diag = colisten.diagonal();
diagonal_sorted = numpy.argsort(-diag)[:500];

#popular_file = open("popular_songs.txt","w");
#for s in diagonal_sorted:
	#popular_file.write(str(s+1));
newFile = open(output_file,'w');

#Each loop takes the song list for one user
for song_count in song_function(test_triplet):
	songs, count = zip(*song_count)
	index=0;
	for every_song in songs:
		colistenArray = colisten[(songs[i]-1),:];
		index+=1;
		number_array = colistenArray.toarray();
		required = number_array.nonzero()[0];
		final_array = numpy.argsort(-(number_array))[0];
		song_list = [];
		for k in range(len(required)):
			if c[k]+1 in songs:
				continue
			song_list.append(str(c[k]+1))
			if len(song_list)==500:
				break
	
	#Now check for the second list for incomplete songs			
	for each_song in diagonal_sorted:
		if str(each_song+1) in songs or str(each_song+1) in song_list:
			continue
		if len(song_list)==500:
			break
		song_list.append(str(song+1));
	newFile.write(' '.join(song_list)+'\n');
	
