#Python matrix builder

import scipy.io
import scipy.sparse
import fileinput
import sys


triplet_file, output_file = sys.argv[1:3]
songs = {};
count=1;
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
		listy.append((song_id,count));
	yield listy;




listener = scipy.sparse.lil_matrix((20,20));

for listy in song_function(triplet_file):
	print(listy);
	for s,_ in listy:
		for f,_ in listy:
			listener[s-1,f-1]+=1;
			print(str(s-1)+","+str(f-1)+"=>"+str(listener[s-1,f-1]));

scipy.io.mmwrite(file(output_file, 'wb'), listener);
print("done");
	
	
