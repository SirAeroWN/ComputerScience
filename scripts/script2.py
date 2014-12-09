with open('test.py', 'a') as myfile:
	j = 1
	k = 1
	for i in range(1,17):
		foo = 'self.btn' + str(i) + ' = Card(\'image/puppy' + str(i) + '.gif\', ' + str(i) + ', \'test\', self.frame, ' + str(j) + ', ' + str(k) + ')\n'
		myfile.write(foo)
		if i % 4 == 0:
			j += 1
		if k % 4 == 0:
			k = 1
		else:
			k += 1