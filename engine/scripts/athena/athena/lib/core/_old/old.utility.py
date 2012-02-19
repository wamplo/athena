#!/usr/bin/env python

# generate_readme
import time

def byte2mb(bytes):
	bytes = float(bytes)
	megabytes = bytes / 1048576
	size = '%.2f MB' % megabytes
	return size;

def generate_readme(where,what = '',desc=''):
	localtime = time.asctime( time.localtime(time.time()) )
	fo = open(where + "readme.txt", "wb")
	fo.write( "Athena BUILD " + what + "\nat " + localtime + "\nworking great! \n" + desc);
	fo.close()