import os
import yaml


class Phonetic:
	def __init__(self):
		self.name_file = os.path.join(os.path.dirname(__file__), 'phonetic_names.yaml')

	def find_name(self, name):
		n = str(name)
		with open(self.name_file, 'r') as f:
			doc = yaml.load(f)

		if doc is not None:
			try:
				return doc[n]['phonetic']
			except KeyError:
				return name.display_name
		else:
			return name.display_name

	def add_phon(self, name, phonetic_sp):
		m = 'added'
		with open(self.name_file, 'r') as f:
			name_list = yaml.load(f)

		try:
			if name_list is not None:
				if name in name_list:
					with open(self.name_file, 'w') as update_f:
						name_list[name]['phonetic'] = phonetic_sp
						yaml.dump(name_list, update_f, default_flow_style=False)
						m = 'updated'
				else:
					with open(self.name_file, 'a') as af:
						data = {}
						data[name] = {
							'phonetic': phonetic_sp
						}
						yaml.dump(data, af, default_flow_style=False)
			else:
				with open(self.name_file, 'w') as nf:
					data = {}
					data[name] = {
						'phonetic': phonetic_sp
					}
					yaml.dump(data, nf, default_flow_style=False)

			return 'Phonetic name {0}. I will now call you {1}'.format(m, phonetic_sp)
		except Exception:
			return 'There was an error. Please try again later.'

	def del_phon(self, name):
		with open(self.name_file, 'r') as f:
			name_list = yaml.load(f)

		if name_list is not None:
			if name in name_list:
				with open(self.name_file, 'w') as rmv:
					del name_list[name]
					yaml.dump(name_list, rmv, default_flow_style=False)
				return 'Your phonetic name has been removed. You will now to refered to by your default name.'
		
		return 'You do not have a phonetic name to remove. If you would like to add one please use: !phonetic_add: YOUR TEXT HERE'