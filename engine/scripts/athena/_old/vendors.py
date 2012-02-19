#!/usr/bin/env python

from anthena.lib.vendors import *

# VENDORS
print('INSTALLING / UPDATEING VENDORS!, WARNING CODE BREAKS!');

# AWAS KALO NAMBAH YANG GAMPANG DIUPDATE AJA KAYA JQUERY DSB, SISAHNYA DIUPDATE MANUAL UNTUK DOKUMENTASI AJA

URL(
	url 		= 'http://code.jquery.com/jquery.min.js',
	filename 	= 'jquery.min.js',
	folder 		= 'jquery'
)

URL(
	url 		= 'https://raw.github.com/defunkt/jquery-pjax/master/jquery.pjax.js',
	filename 	= 'jquery.pjax.js',
	folder 		= 'jquery'
)

''' SEKALI AJA 
HG(
	url 		= 'https://code.google.com/p/pagedown',
	folder 		= 'pagedown',
	name 		= 'PAGEDOWN trunk'
)

GIT(
	url 		= 'git://repo.or.cz/htmlpurifier.git',
	folder 		= 'htmlpurifier',
	name 		= 'HTMLPURIFIER TRUNK'
)

# ganti namespace Vendors\ElephantMarkdown\src\Elephant;
GIT(
	url 		= 'https://github.com/martinvium/ElephantMarkdown.git',
	folder 		= 'elephantmarkdown',
	name 		= 'ElephantMarkdown - Martinvium fork @github'
)
'''

generate_readme(path_vendors,'VENDORS')