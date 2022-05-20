from professor import Professor
from enrol import Enrol

class Course:
	def __init__(self, name, code, max_, min_, professor)
		self.name
		self.code = code
		self.max = max_
		self.min = min_
		self.professor = []
		self.enrollments = []

		if isinstance (professor, Professor):
			self.professors.append(professor)
		elif professor isinstance(professor, list):
			for entry in professor:
				if not isinstance(entry, Professor):
					raise Error("Invaild professor...")

			self.professors = professor
		else:
			raise Error("Invaild professor...")

	def add_professor(self, Professor):
		if not isinstance(professor, Professor):
			raise Error("Invaild professor...")

		self.professors.append(professor)

	def add_enrollment(self, enrol):
		if not isinstance(enrol, Enrol):
			raise Error("Invaild enrol")

		if len(enrollments) == self.max:
			raise Error("Cannot enrol, course is full...")

		self.enrollments.append(enrol)

	def is_cancelled(self):
		return len(self.enrollments) < self.min