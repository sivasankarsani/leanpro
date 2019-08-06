import os
'''
Helper Method for views

'''

def validator_string(query):
	'''
	@param: query
	@type: str

	@rtype: bool
		return True if any case pass
		else False

	1. Check query is nono or not
	2. Check length of query
	3. Check given word had int or not

	'''
	if query is None:
		return True

	if len(query)<1 or not query:
		return True

	if isinstance(query,int):
		return True

	# default response
	return False

def apply_default_filters(_word, _limit=25):
	'''	
	@param: _word
	@type: str

	@param: _limit
	@type: int

	@rtype: dict
		default _word as str and _limit as int with 25

	1. Check type of word and convert into str
	2. Limit is not define, have to set for 25

	'''
	print("limit is ",_limit)
	if not isinstance(_word, str):
		_word = str(_word)
	if not isinstance(_limit, int):
		_limit = int(_limit)

	return {
		"match_word": _word.lower(),
		"limit": _limit
	}

def convert_into_int(num):
	'''
	@param: num
	@type: int

	@rtype: int
	
	1. Convert given num into int if it is str
	'''
	try:
		return int(num)
	except Exception as e:
		return 1

def get_dataset(filename=None):
	"""
	@param: filename [location of dataset file]
	@type: str

	@rtype: dict

	1. get the file_location for dataset
	2. Read the data from dataset
	3. Formating the data set into list of tuples\
		inorder to search in easy way

	4. Return response

	"""
	default_dataset = {
			"status": False,
			"err_msg": "dataset file was not exists"
		}

	# 1. get the file_location for dataset
	if not filename:
		filename = os.getcwd()+'/fuzzysearch/word_search.tsv'

	if not os.path.exists(filename):
		return default_dataset

	#2.Read the data from dataset
	with open(filename,'r') as _f:
		dataset = _f.read()

	# convert dataset into our require format
	all_possible_match_words = []

	for key in dataset.split('\n'):
		each_word = key.split()

		if each_word and each_word[0]:
			tuple_data= (each_word[0], convert_into_int(each_word[1]))
			all_possible_match_words.append(tuple_data)

	if all_possible_match_words:
		return {
			"status": True,
			"all_possible_match_words": all_possible_match_words
		}
	return default_dataset

def filter_best_matched_words(matched_words=[],limit=25):
	"""
	@param: matched_words
	@type: list

	@param: limit
	@type: int

	@rtype: dict

	1. Check matched data is present or not
	2. Sorted the matched words by
		i) By length of word
		ii) By name of word
		iii) By frequencey
	3. Filterd mathed_words upto limit 25
	4. return response

	"""
	if not matched_words or len(matched_words)<1:
		return {
			"status": "failed",
			"data": "No data was found"
		}

	_dataset = sorted(matched_words,key=lambda _word: (len(_word[0]), _word[0], _word[1] ))
	'''
	limit should be positive ow,
	it will return all matched values in reverse order
	'''
	
	data = [_match_word[0] for _match_word in _dataset[:limit]]

	return{
			"status" : "success",
			"data": data
		}




