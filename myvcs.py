#! /usr/bin/python

import os

def backup():
	""" a command line tool that recursively copies everything in the current directory to a directory called .myvcs (which should be created if it doesn't already exist).  At this point it's ok to overwrite .myvcs if it """
	if not os.path.isdir(".myvcs"):
		os.system('mkdir .myvcs')
	subfolder_idx = 1
	while ( os.path.isdir( '.myvcs/' +  str(subfolder_idx) )):
		subfolder_idx += 1
	os.system('mkdir .myvcs/' + str(subfolder_idx) )
	os.system('cp -r * .myvcs/' + str(subfolder_idx))

if __name__ == '__main__':
	backup()



