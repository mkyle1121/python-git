def breakwords(stuff):
	"""This function will break up words."""
	words=stuff.split(' ')
	return words
	
def sortwords(words):
	"""Sorts the words."""
	return sorted(words)
	
def printfirstword(words):
	"""Prints the first words after popping it off."""
	word=words.pop(0)
	print word
	
def printlastword(words):
	"""Prints the last word after popping it off."""
	word=words.pop(-1)
	print word

def sortsentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words=breakwords(sentence)
	return sortwords(words)
	
def printfirstandlast(sentence):
	"""Prints the first and last words of the sentence."""
	words=breakwords(sentence)
	printfirstword(words)
	printlastword(words)
	
def printfirstandlastsorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words=sortsentence(sentence)
	printfirstword=(words)
	printlastword=(words)
	