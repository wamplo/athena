#!/usr/bin/env python

import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

config.add_section('path')
config.set('path', 'path_views', '../../../views/')
config.set('path', 'path_views_cdn', '../../../views_cdn/')
config.set('path', 'path_muncher', 'anthena/bin/muncher/munch')
config.set('path', 'path_optipng', 'anthena/bin/optipng-0.6.5.exe')
config.set('path', 'path_jpegtrans', 'anthena/bin/jpg8dexe/jpegtran.exe')
config.set('path', 'path_googleclosure', 'anthena/bin/googlecc.jar')
config.set('path', 'path_gitftp', 'anthena/lib/core/git-ftp.py')


config.add_section('css')
config.set('css', 'ignore_css', [
	'.a',
	'.typography'
])

# Writing our configuration file to 'example.cfg'
with open('config.cfg', 'wb') as configfile:
    config.write(configfile)