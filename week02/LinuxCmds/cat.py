# cat.py
import sys


def cat(args):
	with open (args[1], 'r') as f:
		data = f.read()

	print(data)


def main():
	cat(sys.argv)



if __name__ == '__main__':
	main()