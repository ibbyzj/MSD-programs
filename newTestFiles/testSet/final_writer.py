#Test final file to write the results for users


import scipy.io
import scipy.sparse
import fileinput
import sys
import numpy

test_output, test_triplet, output_file = sys.argv[1:4]

def song_function(test_triplet):
	old_user = 1;
	listy = [];
	for line in open(test_triplet):
		try:
			user_id = int(line.rstrip('\n').split(' ')[0]);
			song_id = int(line.rstrip('\n').split(' ')[1]);
			count = int(line.rstrip('\n').split(' ')[2]);
		except ValueError:
			continue
		if old_user != user_id:
			yield listy;
			listy = [];
			old_user = user_id;
		listy.append((song_id,count));
	yield listy;




colisten = scipy.io.mmread(file(test_output)).tocsr();
print("done reading matrix");
diag = colisten.diagonal();
diagonal_sorted = numpy.argsort(-diag)[:4];

newFile = open(output_file,'w');

for song_count in song_function(test_triplet):
	songs, count = zip(*song_count)
	print(songs);
	a = colisten[numpy.array(songs)-1,:];
	b=a.toarray();
	c = numpy.argsort(-b);
	song_list = [];
	for oi in c:
		for a in oi:
			if a+1 in songs or a+1 in song_list:
				continue
		song_list.append(str(a+1));
	song_list = list(set(song_list));
	newFile.write(' '.join(song_list)+'\n');
