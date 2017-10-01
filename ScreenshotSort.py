import os, datetime
#Scans the desktop for screenshot filenames and sorts them into a folder
os.chdir("/Users/Amilia/Desktop");
path = os.listdir("Users/Amilia/Desktop");
if not os.path.exists("Users/Amilia/Desktop/Screenshots"):
	os.mkdir("Users/Amilia/Desktop/Screenshots");
for file in path:
	if "Screen Shot" in file:
		os.rename("Users/Amilia/Desktop/"+file , "Users/Amilia/Desktop/Screenshots/"+file);

