#!/usr/bin/env python

gitftp = 'anthena/lib/core/git-ftp.py'

def deploy():
	os.system(gitftp)
	
try:
	import glob
	import os
	import fnmatch
	import sys
	import time

	deploy()


except Exception as inst: # raise e
	print inst
