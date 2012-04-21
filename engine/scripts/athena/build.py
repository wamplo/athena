#!/usr/bin/env python

# Configuration
path_views = '../../../views/'
path_views_cdn = '../../../views_cdn/'

# If development use html instead if production red framework uses PHP /see views/* in redframework
production = 0; 

# Paths
muncher = 'athena/bin/muncher/munch'
optipng = 'athena/bin/optipng-0.7.1.exe'
jpegtrans = 'athena/bin/jpg8dexe/jpegtran.exe' # @todo Compare with cjpeg ?
googleclosure = 'athena/bin/googlecc.jar'

# Place .ignore or #ignore to ignore
ignore_css = [
	'.typography'
]

if production == 0:
	views_ext = 'html' # Html or PHP

if production == 1:
	views_ext = 'php' # Html or PHP

'''
GET VALUES

COMPILE 1
	MOVE

COMPILE 2
	MOVE

COMPILE 3
	MOVE
'''

def compileall():

	''' @TODO NEXT
	config = ConfigParser.ConfigParser()
	config.read('example.cfg')
	path_views = config.get('path', 'path_views', 0)
	path_views_cdn = config.get('path', 'path_views_cdn', 0)
	path_muncher = config.get('path', 'path_muncher', 0)
	path_optipng = config.get('path', 'path_optipng', 0)
	path_jpegtrans = config.get('path', 'path_jpegtrans', 0) # next pake cjpeg
	path_googleclosure = config.get('path', 'path_googleclosure', 0)
	css_ignore = config.get('ignore_css', 'foo', 0)
	'''

	# GET CSS UNCOMPILED
	css = []
	for root, dirname, filenames in os.walk(path_views):
		for filename in fnmatch.filter(filenames, '*.css'):
			css.append(os.path.join(root, filename))

	# GET VIEWS UNCOMPILED
	views = []
	for root, dirname, filenames in os.walk(path_views):
		for filename in fnmatch.filter(filenames, '*.' + views_ext):
			views.append(os.path.join(root, filename))

	# GET PNG UNCOMPILED
	png = []
	for root, dirname, filenames in os.walk(path_views):
		for filename in fnmatch.filter(filenames, '*.png'):
			png.append(os.path.join(root, filename))

	# GET JPG UNCOMPILED
	jpg = []
	for root, dirname, filenames in os.walk(path_views):
		for filename in fnmatch.filter(filenames, '*.jpg'):
			jpg.append(os.path.join(root, filename))

	# GET JS UNCOMPILED
	js = []
	for root, dirname, filenames in os.walk(path_views):
		for filename in fnmatch.filter(filenames, '*.js'):
			js.append(os.path.join(root, filename))	
	
	########### COMPILES ###########

	# REFRESH
	print 'Refreshing'
	shutil.rmtree(path_views_cdn)

	# INIT NEW CDN FOLDERS
	for root, dirname, filenames in os.walk(path_views):
		if not os.path.exists(path_views_cdn + os.path.join(root).split(path_views)[-1]):
				os.makedirs(path_views_cdn + os.path.join(root).split(path_views)[-1])
	
	# CSS AND VIEWS
	cmd = muncher + ' --css ' + ','.join(css) + ' --views ' + ','.join(views) + ' --ignore ' + ','.join(ignore_css)

	# testing
	print 'Building CSS:'
	for css in css:
		print css

	print 'Building VIEWS:'
	for views in views:
		print views
	# testing

	subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	views_compiled = [] # UNTUK README

	print 'Processing CSS + Views'
	for root, dirname, filenames in os.walk(path_views):
		for extension in ('*.opt.' + views_ext, '*.opt.css'):
			for filename in fnmatch.filter(filenames, extension):

				# MOVE OPT.PHP AND OPT.CSS TO NEW CDN FOLDER
				views_compiled.append(os.path.join(root, filename).split(path_views)[-1]) # UNTUK README
				shutil.move(os.path.join(root, filename), path_views_cdn + os.path.join(root, filename).replace('opt.','').split(path_views)[-1])
				
				# IF CSS
				if fnmatch.filter(filenames, '*.opt.css'):
					print 'Optimizing CDN CSS ' + filename.split('.')[0] + '.css'
					minify.css_compress(path_views_cdn + os.path.join(root, filename).replace('opt.','').split(path_views)[-1])
				
				# IF PHP ( HTML )
				if fnmatch.filter(filenames, '*.opt.' + views_ext):
					print 'Optimizing CDN HTML ' + filename.split('.')[0] + '.' + views_ext
					minify.html_compress(path_views_cdn + os.path.join(root, filename).replace('opt.','').split(path_views)[-1])

	# IMAGES
	images_compiled = [] # UNTUK README

	print 'Processing Image'
	for png in png:

		# Debug
		print png.split(path_views)[-1]

		# Start Command
		cmd = optipng + ' ' + png + ' -out ' + os.path.join(path_views_cdn, png.split(path_views)[-1])
		subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		images_compiled.append(png.split(path_views)[-1]) # UNTUK README

	for jpg in jpg:

		# Debug
		print jpg.split(path_views)[-1]

		# Start Command
		cmd = jpegtrans + ' -optimize ' + jpg + ' ' + os.path.join(path_views_cdn, jpg.split(path_views)[-1])
		subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		images_compiled.append(jpg.split(path_views)[-1]) # UNTUK README

	
	# JAVASCRIPT
	js_compiled = [] # UNTUK README
	
	print 'Processing JS'
	for js in js:

		# DEBUG
		print js.split(path_views)[-1]

		# Start Command
		cmd = 'java -jar ' + googleclosure + ' --js ' + js + ' --js_output_file ' + os.path.join(path_views_cdn, js.split(path_views)[-1])
		subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		js_compiled.append(js.split(path_views)[-1]) # UNTUK README

	# OTHERS
	print 'Moving Fonts & GIF'
	#for root, dirname, filenames in os.walk(path_views): ( diatas )
	#MOVE OTHERS TO NEW CDN FOLDER
	for root, dirname, filenames in os.walk(path_views):
		for extension in ('*.ttf','*.otf', '*.gif'): # harus ada salah satu kalo tidak kedelete semua view dan gw ngulang gara2 ini
			for filename in fnmatch.filter(filenames, extension):
				views_compiled.append(os.path.join(root, filename).split(path_views)[-1]) # UNTUK README
				shutil.copyfile(os.path.join(root, filename), path_views_cdn + os.path.join(root, filename).split(path_views)[-1])

	# GENERATE README
	all_compiled = []
	for imagesreadme in images_compiled:
		all_compiled.append(imagesreadme)
	
	for viewsreadme in views_compiled:
		all_compiled.append(viewsreadme)

	for jsreadme in js_compiled:
		all_compiled.append(jsreadme)

	localtime = time.asctime(time.localtime(time.time()))

	# Readme
	print "Generating Readme"
	fo = open(path_views_cdn + "readme.txt", "wb")
	fo.write("Athena BUILD " + "CDN" + "\nat " + localtime + "\n" + "\n".join(all_compiled));
	fo.close()

	# Git Ignore
	if production == 0:
		print "Generating Readme"
		fo = open(path_views_cdn + ".gitignore", "wb")
		fo.write("*\n!.gitignore");
		fo.close()

# LOAD
try:
	import shutil
	import glob
	import os
	import subprocess
	import fnmatch
	import sys
	import time
	import athena.lib.core.minify as minify
	#import ConfigParser @TODO NEXT

	compileall()

except Exception as inst: # raise e
	print inst

