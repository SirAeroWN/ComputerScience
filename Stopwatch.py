#This has a class StopWatch which can be used to create timers

import time

class StopWatch:
	def __init__(self):
		current = time.time()
		self.__startTime = current
		self.__stopTime = current

	def getStart(self):
		return self.__startTime

	def getStop(self):
		return self.__stopTime

	def start(self):
		self.__startTime = time.time()
		return

	def stop(self):
	 	self.__stopTime = time.time()
	 	return

	def ElapsedTime(self):
		elapsedRaw = self.__stopTime - self.__startTime
		elapsedClean = float(format(elapsedRaw, ".3f"))
		elapsedMili = elapsedClean * 1000
		return elapsedMili

timer = StopWatch()
total = 0
timer.start()
for i in range(1, 1000001):
	total += i
timer.stop()
print("That took", timer.ElapsedTime(), "miliseconds")
