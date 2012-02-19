# DOWNLOAD FROM URL
from utility import *
import shutil
import subprocess
import zipfile
import urllib2
import os
import urllib

path_vendors = '../../../vendors/'

def URL(url, filename, folder):

	# GET INFORMATION
	f = urllib2.urlopen(url)
	size = f.headers["Content-Length"]
	print 'updating FILE '+ filename + ' size: ' + byte2mb(size) + ' bytes'

	if not os.path.isdir(path_vendors + folder):
		os.makedirs(path_vendors + folder)

	print 'downloading '+ url + ' to /vendors/' + folder + '/' + filename
	localFile = open(path_vendors + folder + '/' + filename, 'w')
	localFile.write(f.read())
	localFile.close()

# DOWNLOAD FROM ZIP
def ZIP(url, name, folder):

	# GET INFORMATION
	f = urllib2.urlopen(url)
	size = f.headers["Content-Length"]
	print 'updating ZIP '+ name + ' size: ' + byte2mb(size)

	# DELETE EXISTING
	if os.path.isdir(path_vendors + folder):	
		shutil.rmtree(path_vendors + folder)

	if not os.path.isdir(path_vendors + folder):
		os.makedirs(path_vendors + folder)
	
	name, hdrs = urllib.urlretrieve(url, path_vendors + 'temp.zip' )			
	
	z = zipfile.ZipFile(name)
	#z.extractall(path_vendors + folder)
	z.extractall(path_vendors)
	os.unlink(name)

# CLONE HG REPOSITORY
def HG(url, folder, name):

	print 'updating HG '+ name

	if os.path.isdir(path_vendors + folder):	
		shutil.rmtree(path_vendors + folder)

	cmd = 'hg clone ' + url + ' ' + path_vendors + folder
	subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# SECURITY
	shutil.rmtree(path_vendors + folder + '/' + '.hg')

# CLONE GIT REPOSITORY
def GIT(url, folder, name):

	print 'updating GIT '+ name

	if os.path.isdir(path_vendors + folder):	
		shutil.rmtree(path_vendors + folder)

	cmd = 'git clone ' + url + ' ' + path_vendors + folder
	
	# 2 way, unfortunately github doesnt allow this to happen.
	# cmd = git archive --format zip --remote git://repo.or.cz/htmlpurifier.git master --output ../../../vendors/helloworld.zip 
	
	subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# SECURITY
	shutil.rmtree(path_vendors + folder + '/' + '.git')