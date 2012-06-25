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

listenranked = numpy.argsort(-diag)[:500]

with open(output_file, 'w') as out:
	for song_count in song_function(test_triplet):
		songs, count = zip(*song_count)
		sim = numpy.array(count)[numpy.newaxis, :] * colisten[numpy.array(songs) - 1,:]
		simidxs = sim.nonzero()[1]
		srt = numpy.lexsort((-diag[simidxs], -sim[0,simidxs]))
		rankidxs = simidxs[srt]
    
		guess = []
		for s in rankidxs:
			if s+1 in songs:
				continue
			guess.append(str(s+1))
			if len(guess) == 500: break
			else:
				for s in listenranked:
					if s+1 in songs or s+1 in rankidxs:
						continue
				guess.append(str(s+1))
			if len(guess) == 500: break
	print("adding now....");
	out.write(' '.join(guess) + '\n')
