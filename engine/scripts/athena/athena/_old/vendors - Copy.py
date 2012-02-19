#!/usr/bin/env python

''' DUKUNG ZIP, FILE
'TUJUAN FOLDER / FILE' : 'URL KE REPOSITORY / FILE'
UNTUK HG,GIT,SVN DSB HARUS MENAMBAHKAN .EXTENSI DI BELAKANG URL REPOSITORY
MISAL https://code.google.com/p/pagedown menjadi https://code.google.com/p/pagedown.hg

@todo GIT FOLDER, HG FOLDER '''

#import filecmp
# GLOBAL
import urllib2
import os
import urllib

# ZIP
import zipfile

# HG
import shutil
import subprocess

from anthena.lib.utility import *
# filecmp.cmp('file1.txt', 'file1.txt')

vendors = {
	'jquery/jquery.min.js': 'http://code.jquery.com/jquery.min.js',
	'jquery/jquery.pjax.js': 'https://raw.github.com/defunkt/jquery-pjax/master/jquery.pjax.js',
	'htmlpurifier' : 'http://htmlpurifier.org/releases/htmlpurifier-trunk.zip',
	'stackexchange/pagedown' : 'https://code.google.com/p/pagedown.hg'
}

path_vendors = '../../../vendors/'

for key in vendors:
	
	(dirPath, fileName) = os.path.split(path_vendors + key)
	url = vendors[key];

	# IF ITS A ZIP
	if url.split('.')[-1] == 'zip':

		f = urllib2.urlopen(url)
		size = f.headers["Content-Length"]
		print 'Updating ZIP '+ fileName + ' at ' + byte2mb(size)

		if os.path.isdir(dirPath + '/' + fileName):	
			shutil.rmtree(dirPath + '/' + fileName)

		if not os.path.isdir(dirPath + '/' + fileName):
			os.makedirs(dirPath + '/' + fileName)
		
		name, hdrs = urllib.urlretrieve(url, dirPath + '/' + fileName + '.temp.zip' )			
		
		z = zipfile.ZipFile(name)
		z.extractall(dirPath + '/' + fileName)
		os.unlink(name)

	# IF ITS A HG REPOSITORY
	elif url.split('.')[-1] == 'hg':

		print 'Updating HG '+ fileName
		hgurl = url.split('.hg')[0];

		if os.path.isdir(dirPath + '/' + fileName):	
			shutil.rmtree(dirPath + '/' + fileName)

		subprocess.call('hg clone ' + hgurl + ' ' + dirPath + '/' + fileName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		shutil.rmtree(dirPath + '/' + fileName + '/' + '.hg')

	# IF ITS A FILE
	else:
		f = urllib2.urlopen(url)
		size = f.headers["Content-Length"]
		print 'Updating FILE '+ fileName + ' at ' + byte2mb(size) + ' bytes'

		if not os.path.isdir(dirPath):
			os.makedirs(dirPath)

		localFile = open(path_vendors + key, 'w')
		localFile.write(f.read())
		localFile.close()
	
# GENERATE README
# TODO DESC! kaya readme kecil ini apa aja vendor2nya
generate_readme(path_vendors,'VENDORS')