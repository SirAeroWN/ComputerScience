with open('Concentration.py', 'a') as myfile:
	for i in range(1,17):
		foo = '\n\tdef set' + str(i) + '(self):\n\t\tif self.selected == 0:\n\t\t\tself.selected += 1\n\t\t\tself.btn' + str(i) + '["state"] = "disabled"\n\t\t\tself.picNum = ' + str(i) + '\n\t\telse:\n\t\t\tself.selected -= 1\n\t\t\tif(self.checkMatch(' + str(i) + ')):\n\t\t\t\tself.btn' + str(i) + '["state"] = "disabled"\n\t\treturn\n'
		myfile.write(foo)