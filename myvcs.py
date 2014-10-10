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
	os.system('echo ' + str(subfolder_idx) + ' >.myvcs/.latest')
	update_current(str(subfolder_idx))

def checkout(snapshot):
	# check if selected snapshot is valid
	if not os.path.isdir('.myvcs/' + snapshot):
		print 'requested snapshot does not exist'
		exit(0)
	os.system('cp * .myvcs/' + snapshot + '/* ./') 
	update_current(snapshot)

def update_current(snapshot):
	os.system('echo ' + snapshot + ' >.myvcs/head')


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--checkout', help = 'reverts back to selected snapshot')
	parser.add_argument('--latest', action='store_true', help = 'reverts back to the latest snapshot')
	parser.add_argument('--current', action='store_true', help = 'returns a current working snapshot') 
	arg = parser.parse_args()
	if arg.checkout:
		checkout(arg.checkout)
	elif arg.latest:
		try:
			with open('.myvcs/.latest') as f:
				latest = f.read().strip()
				checkout(latest)
		except IOError:
			print '.myvcs/.latest cannot be accessed'
			exit(0)	
		#os.system('find .myvcs/ -type d | sort -n | tail -1 > .latest')
	elif arg.current:
		try:
			with open('.myvcs/head') as f:
				current_snapshot = f.read()
			print current_snapshot
		except IOError:
			print 'cannot open .myvcs/head file'
			exit(0)
	else:
		backup()



