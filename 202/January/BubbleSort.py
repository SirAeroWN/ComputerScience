import random
import time

def bubbleSort(lst):
	swaps = 0
	compares = 0
	needNextPass = True
	k = 1
	while k < len(lst) and needNextPass:
		# List may be sorted and next pass not needed
		needNextPass = False
		for i in range(len(lst) - k):
			compares += 1
			if lst[i] > lst[i + 1]:
				# swap list[i] with list[i + 1]
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
				swaps += 1
				needNextPass = True # Next pass still needed
		k += 1
	print("swaps:", swaps, "\ncomparisons:", compares)

# A test function
def main():
	alist = []
	for i in range(10000):
		alist.append(random.randint(0,10000))
	start = time.time()
	bubbleSort(alist)
	print(format((time.time() - start), '.3f'))

main() # Call the main function