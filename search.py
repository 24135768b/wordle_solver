# guess touch and arise first is a good choice

# input 
words = []
total = 5757 # using 5757 words as the dictionary currently
for i in range(0, total):
	words.append(input())

guess = [] 
# letter 
without = "aresyfgbnmjklio"     # input     
contains = "thu"		# input
for word in words:
	if word[1] == 'u': # and word[4] == 'h':# and word[2] == 'd': # word[1] == 'o': # word[1] == 'o': # word in the right place EX: word[0] == 'a'
		flag_contains = True
		for letter in contains:
			if letter not in word:
				flag_contains = False

		flag_without = True
		for letter in without:
			if letter in word:
				flag_without = False
		
		if flag_without and flag_contains: 
			guess.append(word)

print(guess)
		
	
	