import JSON

directory = r'C:\Users\Lenovo\OneDrive\CodersOnly\PythonF\1 Short Projects\CmdLine_Password\PasswordSaveFile\\'

js = JSON.file(directory + 'password_save_file.json')
password_json_save: dict = js.read()
if password_json_save == 'FileNotFoundError':
	print('FileNotFoundError')
elif password_json_save == 'JSONDecodeError':
	print('JSONDecodeError')

# print(password_json_save)

class password_file_manager:
	user_name = ''
	user_data = ''
	user_data_spec = ''

	def pick_user_name(self, user_name, user_pass=''):
		if user_name in password_json_save['user'] and password_json_save['user'][user_name]['password'] == user_pass:
			self.user_name = user_name
			return f'user {self.user_name} picked'
		else:
			return 'invalid error'

	def pick_user_data(self, user_data):
		if self.user_name == '':
			return 'user name not picked'
		elif user_data not in password_json_save['user'][self.user_name]:
			return 'not found error'
		else:
			self.user_data = user_data
			return f'user data {user_data} picked'

	def pick_user_data_spec(self, user_data_spec):
		if self.user_name == '' and self.user_data == '':
			return 'invalid error'
		elif user_data_spec not in password_json_save['user'][self.user_name][self.user_data]:
			return 'not found error'
		else:
			self.user_data_spec = user_data_spec
			return f'user data specific {user_data_spec} picked'

	def display_data(self):
		if self.user_name != '' and self.user_data != '':
			return f'{self.user_name} > {self.user_data} > {password_json_save["user"][self.user_name][self.user_data]}'
		else:
			return 'invalid error'

	def display_data_spec(self):
		if self.user_name != '' and self.user_data != '' and self.user_data_spec != '':
			return f'{self.user_name} > {self.user_data} > {self.user_data_spec} > {password_json_save["user"][self.user_name][self.user_data][self.user_data_spec]}'
		else:
			return 'invalid error'

ps = password_file_manager()
ps.pick_user_name('Reuben', 'passin')
ps.pick_user_data('gmail')
ps.pick_user_data_spec('email')

print(ps.display_data_spec())

