import sys
import os

def format(size):
	power = 2**10
	n = 0
	power_labels = {0 : '', 1: 'K', 2: 'M', 3 : 'G', 4 : 'T'}
	while size > power:
		size /= power
		n += 1
	return str(int(size)) + power_labels[n]


def duhs(args):
	total_size = 0
	try:
		data = os.statvfs(args)
	except:
		return print("File path no existe")
	print(args,' size is: ',format(data[0]))


def main():
	duhs(sys.argv[1])



if __name__ == '__main__':
	main()