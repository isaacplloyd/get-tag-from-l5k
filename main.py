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
with open(TAG_VALUE_FILE, 'r') as file:
	value_f = file.read()

#Get tag list with data for each tag on a new line
tagdata = extract_taglist_data(base_f)
taglist = tagdata.split('\r\n')
set_values = value_f.split('\n')
first_tag = Tag().from_string(taglist[0])

write_to_file(OUT_FILE, first_tag.value)
print(first_tag.values)
first_tag.set_values(set_values)
print(first_tag.values)
print(first_tag.generate_value_string())
first_tag.set_value_string()
print(first_tag.value)