# words counter: a python script that counts all the words in a sentence
run = True


class word_counter:
	def __init__(self):
		# class variables
		self.ignore = [" ", ","]
		self.input = ""
		self.count = []
		self.counter = []

	def input_sentence(self):
		global run
		# prompts the user for an input
		self.input = input("enter a sentence and I'll count the number of words in it\n")
		# deletes any space at the beginning or at the ending of a sentence 
		self.input = self.input.strip()
		if self.input == "q" or "Q":
			run = False

	def word_count(self):
		for word in self.input:
			if word not in self.ignore:
				self.count.append(word)

			if word in self.ignore:
				if self.count:
					self.counter.append(self.count)
					self.count = []

		if self.count != []:
			self.counter.append(self.count)
			print(self.counter)
			self.count = []

	def no_of_words(self):
		no = str(len(self.counter))
		print("The sentence above contains " + no + " words!")
		self.count = []
		self.counter = []


counter = word_counter()

while run:
	counter.input_sentence()
	counter.word_count()
	counter.no_of_words()
