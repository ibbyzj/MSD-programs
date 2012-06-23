#testing another python program


import _mysql
import sys
import fileinput
import MySQLdb as mdb

file_sort = sys.argv[1:2]


a=[];

counter = 1;
for line in fileinput.input(file_sort):
	user_id = int(line.rstrip('\n').split('\t')[0]);
	song_id = int(line.rstrip('\n').split('\t')[1]);
	count = int(line.rstrip('\n').split('\t')[2]);
	a.append(user_id,song_id,count)
	counter+=1;
	if counter==11:
		print a;
		sys.exit();
