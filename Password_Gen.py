import random

def password_gen(password_length: int=16, needed_keys=None) -> str:
	if needed_keys is None:
		needed_keys = {'digits': True, 'lower_char': True, 'upper_char': True, 'symbols': True}

	def int_ascii(from_num=0, to_num=128) -> list:
		ascii_list = []
		for i in range(from_num, to_num):
			ascii_list.append(chr(i))
		return ascii_list

	digits = int_ascii(48, 58)
	lower_char = int_ascii(97, 123)
	upper_char = int_ascii(65, 91)
	symbols = int_ascii(33, 48) + int_ascii(58, 65) + int_ascii(91, 97) + int_ascii(123, 127)

	password_result = []
	password_keys = []

	password_keys += digits if (needed_keys['digits']) else []
	password_keys += lower_char if (needed_keys['lower_char']) else []
	password_keys += upper_char if (needed_keys['upper_char']) else []
	password_keys += symbols if (needed_keys['symbols']) else []

	for i in range(password_length):
		key_result = password_keys[random.randint(0, len(password_keys) - 1)]
		password_result.append(key_result)

	return ''.join(password_result)


