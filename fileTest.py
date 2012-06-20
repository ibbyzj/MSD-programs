#python file I/O test
import sys
import fileinput
test = open("kaggle_users.txt","r");
newfile = open("kaggle_users_new.txt","w");
count = 1;
for line in fileinput.input(['kaggle_users.txt']):
	temp = line.rstrip('\n');
	newfile.write(temp+" "+str(count)+'\n');
	count=count+1;
test.close();	
newfile.close();
		

