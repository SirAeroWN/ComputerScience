with open('test.py', 'a') as myfile:
	for i in range(1,17):
		foo = 'allTheCards.append(self.btn' + str(i) + ')\n'
		myfile.write(foo)