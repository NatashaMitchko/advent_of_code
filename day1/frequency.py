"""
Day 1: Using a Generator to add numbers
"""

def next_number(filename):
	"""
	Takes a filename, yields the number off the next line
	"""
	with open(filename) as f:
		for line in f:
			yield int(line)

def add_numbers():
	"""
	Given a generator that spits out numbers, add those numbers together
	"""
	nums = next_number("input.txt")

	total = 0
	for n in nums:
		total += n

	return total

if __name__ == '__main__':
	print "The resulting frequency is: "
	print add_numbers()