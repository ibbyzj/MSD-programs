#Python file to add song data to the database and perform sort per user on song counts
# -*- coding: utf-8 -*-

import _mysql
import sys
import fileinput
import MySQLdb as mdb

triplet_file = sys.argv[1:2]

con = None
con = mdb.connect('localhost', 'root','', 'MSD')
counter=1;
for line in fileinput.input(triplet_file):
	user_id = int(line.rstrip('\n').split('\t')[0]);
	song_id = int(line.rstrip('\n').split('\t')[1]);
	count = int(line.rstrip('\n').split('\t')[2]);
	
	cur = con.cursor();

	cur.execute("""INSERT INTO dat VALUES (%s,%s,%s)""",(user_id,song_id,count))
	
con.commit();

con.close();

