from person import Person
from enrol import Enrol

class Student(Person):
	def __init__(self, first, dob, phone, address, international=False):
		super().__init__(self, first, dob, phone, address)
		self.international = international
		self.enrolled = []

	def add_enrollment(self, enrol)
		if not isinstance(enrol, Enrol):
			raise Error("Invaild enrol...")

		self.enrolled.append(enrol)

	def is_on_probation(self):
		return False

	def is_part_time(self):
		return len(self.enrolled) <=3	