#Python file to sort the final triplet for users

import tables
import tables
import sys
import fileinput

input_file, final_triplet_file = sys.argv[1:3]
indi = {};
previous = 1;
for line in fileinput.input([input_file]):
	if str(previous) == (line.rstrip('\n').split(' ')[0]):
		print("came here");
		song_id = line.rstrip('\n').split(' ')[1];
		user_id = line.rstrip('\n').split(' ')[0];
		count = line.rstrip('\n').split(' ')[2];
		
		indi[song_id] = user_id+","+count;
	else:
		print("here?");
		for key in sorted(indi.iterkeys()):
			print "%s: %s" % (key, indi[key])
		sys.exit();
