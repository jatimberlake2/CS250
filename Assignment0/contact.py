#aggregation and inheritance
import sys

class Contact:

	def __init__(self, name, number):
		self._name = name
		self._number = number

	def get_name(self):
		return self._name
	
	def get_number(self):
		return self._number

	def set_name(self, name):
		self._name = name

	def set_number(self, number):
		self._number = number
	
#aggregation
"""
class AddressBookContact:
	
	def __init__(self, name, number, address):
		self._name = name
		self._number = number
		self._address = address

	def getName(self):
		return self._contact.get_name()
	def setName(self, name):
		self._contact.set_name(name)
	def getNumber(self):
		return self._contact.get_number()
	def setNumber(self, number):
		self._contact.set_number(number)
	
	def getAddress(self):
		return self._address
	def setAddress(self, address):
		self._address = address
"""

#inheritance (mo bettuh)
class AddressBookContact(Contact):
		#inherits all Contact methods
	def __init__(self, name, number, address):
		super().__init__(name, number)
		self._address = address
	def getAddress(self):
		return self._address
	def setAddress(self, address):
		self._address = address

def main(argv):
	pb = Contact("Joe", "334")
	print(pb.getName())

if __name__ == '__main__':
	sys.exit(main(sys.argv))
