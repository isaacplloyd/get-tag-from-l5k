class Tag:
	def __init__(self, name='', type='', value=0, length=0, safety=0):
		self.name = name
		self.type = type
		self.length = length
		self.safety = safety
		self.value = value

	#Create tag object from string, optionally starting with '\t' characters
	def from_string(self, input_str):
			name_end = input_str.find(':')
			self.name = input_str[:name_end]
			type_end = input_str.find('(')
			self.type = input_str[name_end+1:type_end]
			value_start = input_str.find('):=') + 3
			self.value = input_str[value_start:]
			return self
		
def find_tag_start(file_contents):
	return file_contents.find('\n\tTAG') + 7

def find_tag_end(file_contents, beginning):
	return file_contents.find('\n\tEND_TAG', beginning) - 1

def extract_taglist_data(file_contents):
	start = find_tag_start(file_contents)
	end = find_tag_end(file_contents, start)
	taglist_data = file_contents[start:end]
	formatted_taglist = format_taglist(taglist_data)
	return formatted_taglist

def format_taglist(in_str):
	#get rid of all existing whitespace and ';' and put each tag on its own line
	out_str = in_str.replace(" ", "")
	out_str = out_str.replace("\r","")
	out_str = out_str.replace("\n","")
	out_str = out_str.replace("\t","")
	out_str = out_str.replace(";","\r\n")
	return out_str
	
def get_next_tag_str(in_str):
	line_end = in_str.find('\r\n')
	return in_str[:line_end]

def write_to_file(filename, contents):
	with open(filename, 'w+') as file:
		file.write(contents)