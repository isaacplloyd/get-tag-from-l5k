'''
Set filenames, etc. in cfg.py
'''

from cfg import *		#import config variables
from tag import *		#import tag function/function definitions
import os
import codecs

#read in base file contents
with codecs.open(BASE_FILE, 'r', encoding='utf8') as file:
	base_f = file.read()

#Get tag list with data for each tag on a new line
tagdata = extract_taglist_data(base_f)
taglist = tagdata.split('\r\n')
tags = ['','','','','','']
for i in range(0, 5):
	tags[i] = (Tag().from_string(taglist[i]))
	print(tags[i].name,tags[i].type, tags[i].value)

#first_tag = Tag().from_string(next_tag_str)

#write_to_file(OUT_FILE, taglist_formatted)
#write_to_file(OUT_FILE, next_tag_str)

taglist = {}
#taglist.add(