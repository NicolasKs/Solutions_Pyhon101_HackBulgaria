import sys


def reduce_file_path(path):
	p_list = [char for char in path]
	i = 0
	try:
		while i < len(p_list):
			if p_list[i] == p_list[i + 1] and p_list[i] == '/':
				p_list.pop(i+1)
				i -= 1
			i += 1
	except:
		print('kaval')

	print(p_list)


def main():
	reduce_file_path(sys.argv[1])



if __name__ == '__main__':
	main()