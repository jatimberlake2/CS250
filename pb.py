import sys

class Phonebook:
	#Method (constructor)
	def __init__(self):
		self._entries = [] #private
	#methods (mutator)
	def add_entry(self, name, number):
		self._entries.append([name, number])
	#accessor/query methods
	def lookup(self, name):
		for entry in self._entries:
			if entry[0] == name:
				return entry[1]
		return "Private Number"
	def reverse_lookup(self, number):
		for entry in self._entries:
			if entry[1] == number:
				return entry[0]
		return "Unknown"
	def size(self)
		return len(self._entries)

	#special methods
	def __str__(self)
		s = ''
		for entry in self._entries:
			s += entry[0] + ' ' + entry[1] + +'\n'
		return s

def main(argv):
	pb = PhoneBook()
	pb.add_entry("Nicholas Kraft", "205-555-5555")
	pb.add_entry("Elizabeth Williams", "256-555-5555")
	print(pb, end='')
	print(str(pb), end='')
	print(pb.lookup("Nicholas Kraft"))
	print(pb.lookup("Jonathan Corley"))
	print(pb.reverse_lookup("256-555-5555"))
	print(pb.reverse_lookup("812-555-5555"))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
