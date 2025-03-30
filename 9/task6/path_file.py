import os


def path_p(derektory,nam_f=''):
	path=os.path.join(derektory[0],derektory[1],nam_f)
	file_n_path=os.path.abspath(path).replace('\\','\\\\')
	return file_n_path