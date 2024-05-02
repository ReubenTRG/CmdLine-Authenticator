"""
To work with json files to read data
"""

import json


class file:
	jsonFilePath = ''
	data = {}

	def __init__(self, jsonFilePath):
		self.jsonFilePath = jsonFilePath

	def read(self):
		try:
			with open(self.jsonFilePath, 'r') as jsonFile:
				self.data = json.load(jsonFile)

			return self.data

		except FileNotFoundError:
			return 'FileNotFoundError'

		except json.JSONDecodeError:
			return 'JSONDecodeError'

	def write(self, jsonData=None):
		try:
			if jsonData is None:
				jsonData = self.data
			else:
				self.data = jsonData

			with open(self.jsonFilePath, 'w') as jsonFile:
				json.dump(jsonData, jsonFile, indent=2)

		except json.JSONDecodeError:
			return 'JSONDecodeError'

	def default(self, defList: list) -> bool:
		for i in defList:
			if i not in self.data:
				return False
		return True
