import json
from difflib import get_close_matches

# load dictionairy from json file
data = json.load(open("data.json"))

# Find the 
def search(word):
	lower_word = word.lower()
	if lower_word in data:
		return data[word]
	elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
	elif len(get_close_matches(lower_word, data.keys())) > 0:
		TRUTH_SENTINEL = "Y"
		FALSE_SENTINEL = "N"
		i = 0
		while i < len(get_close_matches(lower_word, data.keys())): #checks through words with a close spelling
			close_word = get_close_matches(lower_word, data.keys())[i]
			print("Did you mean {0} instead?".format((close_word)))
			is_word = input("Input {0} for yes and {1} for no: ".format(TRUTH_SENTINEL, FALSE_SENTINEL))
			if is_word.upper() == TRUTH_SENTINEL:
				return data[close_word]
			elif is_word.upper() == FALSE_SENTINEL:
				i += 1
			else:
				print("Please ensure you entered either {0} or {1}".format(TRUTH_SENTINEL, FALSE_SENTINEL)) #Bad user input
	else:
		return "Please ensure you entered the correct word." #Word not found


run_sentinel = "X"
search_term = ""

while run_sentinel != search_term:
	search_term = str(input("Enter word or 'X' when finished: "))
	defintion_list = search(search_term)
	print("\n".join(defintion_list))