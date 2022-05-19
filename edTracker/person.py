from address import Address

class Person:
	def __init__(self, first, dob, phone, address):
		self.first_name = first
		self.last_name = last
		self.date_of_birth = dob
		self.phone = phone
		self.addresses = []

		if address is isinstance (address, Address):
			self.addresses.append(address)
		elif address isinstance(address, list):
			for entry in address:
				if not isinstance(entry, Address):
					raise Error("Invaild Address...")

			self.addresses = address
		else:
			raise Error("Invaild Address...")
	
	def add_address(self, address):
		if not isinstance(address, Address):
			raise Error("Invaild Address...")
		self.addresses.append(address)		