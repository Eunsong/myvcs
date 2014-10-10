#! /usr/bin/python

import os

def single_backup():
	""" a command line tool that recursively copies everything in the current directory to a directory called .myvcs (which should be created if it doesn't already exist).  At this point it's ok to overwrite .myvcs if it """
	if not os.path.isdir(".myvcs"):
		os.system('mkdir .myvcs')
	else:
		""" remove everything in .myvcs """
		os.system('rm .myvcs/*')
	os.system('cp -r * .myvcs/')

if __name__ == '__main__':
	single_backup()



