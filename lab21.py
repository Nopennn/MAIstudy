import os
import sys
print('Введите суффикс\n')
suffix_name = str(input())
a = len(suffix_name)
file_name = 'g'
print('Вводите файлы с двумя и более связями. Введите 0, чтобы закончить\n')
while file_name != '0':	
	file_name = str(input())
	if(file_name != '0'):
		if(suffix_name == file_name[a-1:]):
			new = file_name.replace(suffix_name, "")
			suf = suffix_name.replace(".", "")
			f = open(suf + new, 'x')
		else:
			print('Суффикс этого файла не соответствует введённому суффиксу\n')

