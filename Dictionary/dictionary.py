import json

# load dictionairy from json file
data = json.load(open("data.json"))

# Find the 
def search():
	word = str(input("Enter word: "))
	lower_word = word.lower()
	if lower_word in data:
		return data[word]
	else:
		return "Please ensure you entered the correct word." #Word not found

print(search())
