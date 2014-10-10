#! /usr/bin/python

import os
import argparse

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
	parser = argparse.ArgumentParser()
	parser.add_argument('--checkout', help = 'reverts back to selected snapshot')
	arg = parser.parse_args()
	if arg.checkout:
		# check if selected snapshot is valid
		if not os.path.isdir('.myvcs/' + org.checkout):
			print 'requested snapshot does not exist'
			os.exit(0)
		os.system('cp * .myvcs/' + arg.checkout + '/* ./') 
	else:
		backup()
