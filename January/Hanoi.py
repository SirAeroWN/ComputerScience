def foo(ndisks):
	def hanoi(ndisks, startPeg='A', endPeg='C', auxPeg = 'B'):
	    global count
	    if ndisks:
	        hanoi(ndisks-1, startPeg, auxPeg, endPeg)
	        #print("Move disk {0} from peg {1} to peg {2}"  .format(ndisks, startPeg, endPeg))
	        count +=1
	        hanoi(ndisks-1, auxPeg, endPeg, startPeg)

	from time import clock,time
	global count
	count = 0
	start = time()


	hanoi(ndisks)
	elapsed = (time() - start)
	print( "\n{0} moves in {1} seconds" .format(count, elapsed))
	try:
		print( "There were {0} moves per second ({1} disks)" .format(count/elapsed, ndisks))
	except ZeroDivisionError:
		print("That was really freaking fast. There were {0} moves for {1} disks" .format(count, ndisks))

for i in range(3, 1000):
	foo(i)