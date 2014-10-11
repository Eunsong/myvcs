#! /usr/bin/python

import os
import argparse
import time

def backup():
	if not os.path.isdir(".myvcs"):
		os.system('mkdir .myvcs')
		os.system('echo 1'+ '>.myvcs/.latest')
	snapshot_version = get_latest() + 1
	os.system('mkdir .myvcs/' + str(snapshot_version) )
	os.system('cp -r * .myvcs/' + str(snapshot_version))
	os.system('echo ' + str(snapshot_version) + ' >.myvcs/.latest')
	update_current(str(snapshot_version))
	datetime = time.strftime("%D-%H:%M:%S")
	os.system('echo ' + datetime + '>.myvcs/' + str(snapshot_version) + '/.date')

def backup_with_message(msg):
	""" do backup and leave message that passed in """
	pass

def checkout(snapshot):
	# check if selected snapshot is valid
	if not os.path.isdir('.myvcs/' + snapshot):
		print 'requested snapshot does not exist'
		exit(0)
	os.system('cp * .myvcs/' + snapshot + '/* ./') 
	update_current(snapshot)

def update_current(snapshot):
	os.system('echo ' + snapshot + ' >.myvcs/head')

def get_latest():
	try:
		with open('.myvcs/.latest') as f:
			latest = int(f.read().strip())
			return latest
	except IOError:
		print 'error:inaccessible .myvcs/.latest file'
		exit(0)

def get_current():
	try:
		with open('.myvcs/head') as f:
			current_snapshot = f.read()
		return current_snapshot
	except IOError:
		print 'cannot open .myvcs/head file'
		exit(0)

def log():
	"""
		print a list of the backups & their creation dates
	"""
	latest = get_latest()
	for i in range(1, latest+1):
		try:
			path = '.myvcs/' + str(i)
			print '\nsnapshot #%d : ' %i,
			_print_log(path)
		except IOError:
			pass	

def _print_log(path):
	# get message if exists
	try:
		with open(path + '/.message') as f:
			msg = f.read().strip()
			print msg + ' ',
	except IOError:
		pass
	os.system('ls ' + path + '>.tmplist')
	files = ''
	with open('.tmplist') as f:
		files = f.read()
	os.system('rm .tmplist')
	tokens = files.strip().split()
	with open(path + '/.date') as f:
		datetime = f.read()
	print datetime.strip() + ' ',
	for each_file in tokens:
		print each_file + ' ',

	
def write_message(path, msg):
	os.system('echo ' + msg + '>' + path + '/.message')


	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--checkout', help = 'reverts back to selected snapshot')
	parser.add_argument('--latest', action='store_true', help = 'reverts back to the latest snapshot')
	parser.add_argument('--current', action='store_true', help = 'returns a current working snapshot') 
	parser.add_argument('--log', action='store_true', help = 'prints out log info')
	parser.add_argument('--message', '-m', help = 'leave a note about this backup')
	arg = parser.parse_args()
	if arg.checkout:
		checkout(arg.checkout)
	elif arg.latest:
		latest = str(get_latest())
		checkout(latest)
		#os.system('find .myvcs/ -type d | sort -n | tail -1 > .latest')
	elif arg.current:
		print get_current()
	elif arg.log:
		log()
	else:
		backup()
		if arg.message:
			try:
				write_message('.myvcs/' + str(get_latest()), arg.message)
			except IOError:
				print '.myvcs/.latest file cannot be accessed'
				exit(0)



