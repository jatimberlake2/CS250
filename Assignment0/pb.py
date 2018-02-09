import sys
from contact import Contact

class Phonebook:

	# Special Method (**Constructor**)
	def __init__(self):
		self._entries = [] # private field named entries

	# Method (Mutator)
	def add_entry(self, name, number):
		entry = Contact(name, number)
		self._entries.append(entry)
			
	# Method (Accessor/Query)
	def lookup(self, name):
		for entry in self._entries:
			if entry.get_name() == name:
				return entry.get_number()
		return "Private Number"

	# Method (Accessor/Query)
	def reverse_lookup(self, number):
		for entry in self._entries:
			if entry.get_number() == number:
				return entry.get_name()
		return "Unknown"

	# Method (Accessor/Query)
	def size(self):
		return len(self._entries)

	# Special Method
	def __str__(self):
		s = ''
		for entry in self._entries:
			s += str(entry.get_name()) + ' ' + str(entry.get_number()) + '\n'
		return s


def main(argv):
	pb = Phonebook() # calls Phonebook.__init__
	pb.add_entry("Nicholas Kraft", "205-555-5555")
	pb.add_entry("Elizabeth Williams", "256-555-5555")
	#print(pb, end='') # calls Phonebook.__str__
	print(str(pb), end='') # equivalent to line 43
	print(pb.lookup("Nicholas Kraft"))
	print(pb.lookup("Jonathan Corley"))
	print(pb.reverse_lookup("256-555-5555"))
	print(pb.reverse_lookup("812-555-5555"))
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
